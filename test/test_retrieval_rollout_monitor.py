import json
from datetime import date, timedelta
from pathlib import Path

import pytest

from scripts.monitor_retrieval_rollout import RolloutGuardError, collect_once, evaluate_window, main


THRESHOLDS = {
    "forbidden_assertion_count_max": 0,
    "strict_nutrition_misclaim_count_max": 0,
    "rollout": {"error_rate_delta_max": 0.01, "p95_latency_ratio_max": 1.2},
}


def _sample(timestamp, variant, *, error_count=0, p95=100):
    return {
        "timestamp": f"{timestamp.isoformat()}T12:00:00+00:00",
        "variant": variant,
        "config_hash": "a" * 64,
        "request_count": 20,
        "error_count": error_count,
        "p95_latency_ms": p95,
        "forbidden_assertion_count": 0,
        "strict_nutrition_misclaim_count": 0,
    }


def test_collect_once_enforces_authorized_source_and_immutability(tmp_path):
    source_root = tmp_path / "approved"
    source_root.mkdir()
    source = source_root / "metrics.json"
    source.write_text(json.dumps(_sample(date(2026, 8, 1), "old")), encoding="utf-8")
    artifact_dir = tmp_path / "artifacts"

    result = collect_once(source=source, source_root=source_root, artifact_dir=artifact_dir, variant="old")
    assert result["status"] == "sampled"
    with pytest.raises(RolloutGuardError, match="不可变"):
        collect_once(source=source, source_root=source_root, artifact_dir=artifact_dir, variant="old")
    outside = tmp_path / "outside.json"
    outside.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    with pytest.raises(RolloutGuardError, match="允许根目录"):
        collect_once(source=outside, source_root=source_root, artifact_dir=artifact_dir, variant="old")


def test_evaluate_requires_real_seven_day_window_and_keeps_legacy_when_blocked(tmp_path):
    artifact_dir = tmp_path / "artifacts"
    artifact_dir.mkdir()
    report = evaluate_window(artifact_dir=artifact_dir, thresholds=THRESHOLDS, window_days=7, min_requests=100)
    assert report["status"] == "blocked"
    assert "no_samples" in report["errors"]
    assert report["recommended_action"] == "keep_legacy_traffic"


def test_personal_local_profile_does_not_require_online_window(tmp_path):
    report = evaluate_window(artifact_dir=tmp_path / "artifacts", thresholds={"deployment_profile": "personal-local"}, window_days=7, min_requests=100)
    assert report["status"] == "not_applicable"
    assert report["valid"] is True
    assert report["recommended_action"] == "offline_evaluation_only"


def test_cli_allows_relative_thresholds_path(tmp_path, monkeypatch):
    thresholds = tmp_path / "thresholds.json"
    thresholds.write_text(json.dumps({"deployment_profile": "personal-local"}), encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    assert main([
        "--evaluate",
        "--artifact-dir", str(tmp_path / "artifacts"),
        "--thresholds", "thresholds.json",
        "--profile", "personal-local",
    ]) == 0


def test_explicit_protected_profile_overrides_local_thresholds_and_rejects_nan(tmp_path):
    artifact_dir = tmp_path / "artifacts"
    artifact_dir.mkdir()
    report = evaluate_window(artifact_dir=artifact_dir, thresholds={"deployment_profile": "personal-local"}, window_days=7, min_requests=100, profile="protected")
    assert report["status"] == "blocked"

    source_root = tmp_path / "approved"
    source_root.mkdir()
    source = source_root / "metrics.json"
    source.write_text(json.dumps({**_sample(date(2026, 8, 1), "old"), "p95_latency_ms": float("nan")}), encoding="utf-8")
    with pytest.raises(RolloutGuardError, match="非负数字"):
        collect_once(source=source, source_root=source_root, artifact_dir=artifact_dir, variant="old")


def test_evaluate_passes_only_with_old_baseline_and_full_window(tmp_path):
    artifact_dir = tmp_path / "artifacts"
    artifact_dir.mkdir()
    start = date(2026, 8, 1)
    for offset in range(7):
        current = start + timedelta(days=offset)
        for variant in ("old", "new"):
            sample = _sample(current, variant, error_count=0, p95=110 if variant == "new" else 100)
            (artifact_dir / f"sample-{offset}-{variant}.json").write_text(json.dumps(sample), encoding="utf-8")

    report = evaluate_window(artifact_dir=artifact_dir, thresholds=THRESHOLDS, window_days=7, min_requests=100)
    assert report["valid"] is True
    assert report["status"] == "passed"
    assert report["comparison"]["p95_latency_ratio"] == 1.1
    assert json.loads((artifact_dir / "rollout-window.json").read_text(encoding="utf-8"))["status"] == "passed"
