#!/usr/bin/env python3
"""采集和评估检索渐进 rollout 的不可变本地守卫。

指标源必须是已授权根目录内的 JSON 文件。脚本只读取指标源，不启动服务、不切换
流量；没有足够的真实时间窗口时始终输出 blocked 并建议保持旧路径。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any


class RolloutGuardError(ValueError):
    """指标源、artifact 或 rollout 窗口不满足安全契约。"""


_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _absolute_path(value: str, label: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise RolloutGuardError(f"{label} 必须是绝对路径")
    return path.resolve()


def _within(path: Path, root: Path, label: str) -> Path:
    try:
        path.relative_to(root)
    except ValueError as error:
        raise RolloutGuardError(f"{label} 不在允许根目录内") from error
    return path


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _atomic_json(path: Path, value: dict[str, Any]) -> None:
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as temporary:
        json.dump(value, temporary, ensure_ascii=False, sort_keys=True, indent=2)
        temporary.write("\n")
        temporary.flush()
        os.fsync(temporary.fileno())
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, path)


def _parse_timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise RolloutGuardError("指标 timestamp 必须是 ISO-8601 字符串")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise RolloutGuardError("指标 timestamp 不是合法 ISO-8601") from error
    if parsed.tzinfo is None:
        raise RolloutGuardError("指标 timestamp 必须带时区")
    return parsed.astimezone(timezone.utc)


def _load_object(path: Path, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RolloutGuardError(f"{label} 不是有效 JSON: {error}") from error
    if not isinstance(payload, dict):
        raise RolloutGuardError(f"{label} 必须是 JSON 对象")
    return payload


def _validate_sample(sample: dict[str, Any], *, requested_variant: str | None = None) -> dict[str, Any]:
    variant = sample.get("variant")
    if variant not in {"old", "new"} or (requested_variant and variant != requested_variant):
        raise RolloutGuardError("指标 variant 必须与 old/new 且与请求一致")
    timestamp = _parse_timestamp(sample.get("timestamp"))
    config_hash = sample.get("config_hash")
    if not isinstance(config_hash, str) or not _SHA256.fullmatch(config_hash):
        raise RolloutGuardError("指标 config_hash 必须是 64 位 SHA-256")
    numeric_fields = ("request_count", "error_count", "p95_latency_ms", "forbidden_assertion_count", "strict_nutrition_misclaim_count")
    for field in numeric_fields:
        value = sample.get(field)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(float(value)) or value < 0:
            raise RolloutGuardError(f"指标 {field} 必须是非负数字")
    if sample["error_count"] > sample["request_count"]:
        raise RolloutGuardError("error_count 不能大于 request_count")
    normalized = dict(sample)
    normalized["timestamp"] = timestamp.isoformat().replace("+00:00", "Z")
    normalized["variant"] = variant
    return normalized


def collect_once(*, source: Path, source_root: Path, artifact_dir: Path, variant: str, config_hash: str | None = None) -> dict[str, Any]:
    source = _within(_absolute_path(str(source), "metrics-source"), _absolute_path(str(source_root), "allowed-metrics-root"), "metrics-source")
    artifact_dir = _absolute_path(str(artifact_dir), "artifact-dir")
    if not source.is_file():
        raise RolloutGuardError("metrics-source 不存在或不是文件")
    sample = _validate_sample(_load_object(source, "metrics-source"), requested_variant=variant)
    if config_hash is not None:
        if not _SHA256.fullmatch(config_hash):
            raise RolloutGuardError("config-hash 必须是 64 位 SHA-256")
        sample["config_hash"] = config_hash
    sample["source_alias"] = source.name
    sample["source_sha256"] = _sha256_bytes(source.read_bytes())
    sample["collected_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    artifact_name = f"sample-{sample['timestamp'].replace(':', '').replace('-', '')}-{variant}.json"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = artifact_dir / artifact_name
    if artifact_path.exists():
        raise RolloutGuardError("不可变指标 artifact 已存在，拒绝覆盖")
    _atomic_json(artifact_path, sample)
    return {"status": "sampled", "artifact": artifact_path.name, "variant": variant, "source_alias": source.name}


def _read_artifacts(artifact_dir: Path) -> list[dict[str, Any]]:
    if not artifact_dir.is_dir():
        raise RolloutGuardError("artifact-dir 不存在或不是目录")
    artifacts = []
    for path in sorted(artifact_dir.glob("sample-*.json")):
        artifacts.append(_validate_sample(_load_object(path, path.name)))
    return artifacts


def _aggregate(samples: list[dict[str, Any]]) -> dict[str, Any]:
    requests = sum(float(item["request_count"]) for item in samples)
    errors = sum(float(item["error_count"]) for item in samples)
    return {
        "sample_count": len(samples),
        "request_count": int(requests),
        "error_count": int(errors),
        "error_rate": errors / requests if requests else None,
        "p95_latency_ms": max(float(item["p95_latency_ms"]) for item in samples),
        "forbidden_assertion_count": sum(int(item["forbidden_assertion_count"]) for item in samples),
        "strict_nutrition_misclaim_count": sum(int(item["strict_nutrition_misclaim_count"]) for item in samples),
        "config_hashes": sorted({item["config_hash"] for item in samples}),
    }


def evaluate_window(*, artifact_dir: Path, thresholds: dict[str, Any], window_days: int, min_requests: int, output: Path | None = None, profile: str | None = None) -> dict[str, Any]:
    profile = profile or str(thresholds.get("deployment_profile", "protected"))
    artifact_dir = _absolute_path(str(artifact_dir), "artifact-dir")
    if profile == "personal-local":
        report = {
            "status": "not_applicable",
            "valid": True,
            "profile": profile,
            "window": {"window_days": 0, "min_requests": 0, "first_date": None, "last_date": None, "calendar_days": 0},
            "aggregates": {},
            "comparison": None,
            "errors": [],
            "recommended_action": "offline_evaluation_only",
            "reason": "个人本地项目不接入真实流量，使用冻结离线评测作为发布依据",
        }
        artifact_dir.mkdir(parents=True, exist_ok=True)
        output = _absolute_path(str(output or artifact_dir / "rollout-window.json"), "rollout-window")
        if output.parent != artifact_dir:
            raise RolloutGuardError("rollout-window 必须写入 artifact-dir")
        _atomic_json(output, report)
        return report
    artifacts = _read_artifacts(artifact_dir)
    errors = []
    if not artifacts:
        errors.append("no_samples")
    dates = sorted({_parse_timestamp(item["timestamp"]).date() for item in artifacts})
    if dates and (dates[-1] - dates[0]).days + 1 < window_days:
        errors.append("window_days")
    if dates and len(dates) < window_days:
        errors.append("missing_calendar_days")
    aggregates = {}
    for variant in ("old", "new"):
        samples = [item for item in artifacts if item["variant"] == variant]
        if samples:
            aggregates[variant] = _aggregate(samples)
    new_metrics = aggregates.get("new")
    old_metrics = aggregates.get("old")
    if new_metrics is None:
        errors.append("missing_new_variant")
    elif new_metrics["request_count"] < min_requests:
        errors.append("min_requests")
    if old_metrics is None:
        errors.append("missing_old_baseline")
    if new_metrics:
        if new_metrics["forbidden_assertion_count"] > thresholds.get("forbidden_assertion_count_max", 0):
            errors.append("forbidden_assertion_count")
        if new_metrics["strict_nutrition_misclaim_count"] > thresholds.get("strict_nutrition_misclaim_count_max", 0):
            errors.append("strict_nutrition_misclaim_count")
    comparison = None
    rollout_thresholds = thresholds.get("rollout", {})
    if new_metrics and old_metrics and old_metrics["error_rate"] is not None:
        comparison = {
            "error_rate_delta": new_metrics["error_rate"] - old_metrics["error_rate"],
            "p95_latency_ratio": new_metrics["p95_latency_ms"] / old_metrics["p95_latency_ms"] if old_metrics["p95_latency_ms"] else None,
        }
        if comparison["error_rate_delta"] > rollout_thresholds.get("error_rate_delta_max", 0.01):
            errors.append("error_rate_delta")
        if comparison["p95_latency_ratio"] is None or comparison["p95_latency_ratio"] > rollout_thresholds.get("p95_latency_ratio_max", 1.2):
            errors.append("p95_latency_ratio")
    report = {
        "status": "passed" if not errors else "blocked",
        "valid": not errors,
        "window": {"window_days": window_days, "min_requests": min_requests, "first_date": dates[0].isoformat() if dates else None, "last_date": dates[-1].isoformat() if dates else None, "calendar_days": len(dates)},
        "aggregates": aggregates,
        "comparison": comparison,
        "errors": sorted(set(errors)),
        "recommended_action": "keep_new_allowlist" if not errors else "keep_legacy_traffic",
    }
    if output is None:
        output = _absolute_path(str(artifact_dir / "rollout-window.json"), "rollout-window")
    else:
        output = _absolute_path(str(output), "rollout-window")
    if output.parent != artifact_dir:
        raise RolloutGuardError("rollout-window 必须写入 artifact-dir")
    _atomic_json(output, report)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--once", action="store_true")
    modes.add_argument("--evaluate", action="store_true")
    parser.add_argument("--metrics-source", type=Path)
    parser.add_argument("--allowed-metrics-root", type=Path)
    parser.add_argument("--variant", choices=("old", "new"))
    parser.add_argument("--config-hash")
    parser.add_argument("--artifact-dir", required=True, type=Path)
    parser.add_argument("--thresholds", type=Path)
    parser.add_argument("--window-days", type=int, default=7)
    parser.add_argument("--min-requests", type=int, default=100)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--profile", choices=("protected", "personal-local"))
    args = parser.parse_args(argv)
    if args.once:
        if not args.metrics_source or not args.allowed_metrics_root or not args.variant:
            parser.error("--once 必须提供 --metrics-source、--allowed-metrics-root 和 --variant")
        result = collect_once(source=args.metrics_source, source_root=args.allowed_metrics_root, artifact_dir=args.artifact_dir, variant=args.variant, config_hash=args.config_hash)
    else:
        if not args.thresholds:
            parser.error("--evaluate 必须提供 --thresholds")
        thresholds = _load_object(_absolute_path(str(args.thresholds), "thresholds"), "thresholds")
        profile = args.profile or thresholds.get("deployment_profile", "protected")
        result = evaluate_window(artifact_dir=args.artifact_dir, thresholds=thresholds, window_days=args.window_days, min_requests=args.min_requests, output=args.output, profile=profile)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result.get("valid", result.get("status") == "sampled") else 2


if __name__ == "__main__":
    raise SystemExit(main())
