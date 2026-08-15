"""Pure helpers for the frozen single-judge answer-quality evaluation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCORE_FIELDS = (
    "task_score",
    "preference_score",
    "evidence_expression_score",
    "boundary_expression_score",
    "readability_score",
)


class ScoreValidationError(ValueError):
    """Raised when a judge reply cannot become a valid scorecard entry."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def answer_type(case_id: str) -> str:
    scenario, difficulty, _ = case_id.split("-", 2)
    if scenario in {"S06", "S07"}:
        return "recommendation"
    if scenario in {"S08", "S09", "S10"} or (scenario == "S05" and difficulty == "C"):
        return "refusal_or_degraded"
    return "normal"


def applicable_dimensions(kind: str, rubric: dict[str, Any]) -> list[str]:
    return [field for field, weight in rubric["weights"][kind].items() if weight is not None]


def validate_and_score(
    reply: dict[str, Any],
    kind: str,
    rubric: dict[str, Any],
    schema: dict[str, Any],
    evidence_ids: set[str],
) -> dict[str, Any]:
    errors = sorted(Draft202012Validator(schema).iter_errors(reply), key=lambda error: list(error.path))
    if errors:
        raise ScoreValidationError("schema: " + "; ".join(error.message for error in errors))
    weights = rubric["weights"][kind]
    total = 0.0
    for field in SCORE_FIELDS:
        value = reply[field]
        weight = weights[field]
        if weight is None and value is not None:
            raise ScoreValidationError(f"{field} must be null for {kind}")
        if weight is not None and (not isinstance(value, int) or not 1 <= value <= 5):
            raise ScoreValidationError(f"{field} must be an integer from 1 to 5 for {kind}")
        if weight is not None:
            total += weight * (value - 1) / 4
    for note in reply["evidence_notes"]:
        unknown = set(note["evidence_ids"]) - evidence_ids
        if unknown:
            raise ScoreValidationError("unknown evidence IDs: " + ", ".join(sorted(unknown)))
    scored = dict(reply)
    scored["total_score_100"] = round(total, 2)
    return scored


def json_line_append(path: Path, value: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
