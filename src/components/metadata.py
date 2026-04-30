"""Component E: metadata agreement similarity."""

from __future__ import annotations

from typing import Any, Iterable


def _norm_meta_val(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, str):
        return v.strip().lower()
    return v


def metadata_similarity(metadata_a: dict[str, Any], metadata_b: dict[str, Any], fields: Iterable[str]) -> tuple[float, list[dict[str, Any]]]:
    """Field-wise metadata agreement with null-handling rules."""
    rows = []
    matches = 0
    counted = 0
    for f in fields:
        va, vb = metadata_a.get(f), metadata_b.get(f)
        if va is None and vb is None:
            rows.append({"field": f, "a": va, "b": vb, "included": False})
            continue
        counted += 1
        if va is None or vb is None:
            ok = False
        else:
            na, nb = _norm_meta_val(va), _norm_meta_val(vb)
            if isinstance(va, (int, float)) and isinstance(vb, (int, float)):
                ok = float(va) == float(vb)
            else:
                ok = na == nb
        if ok:
            matches += 1
        rows.append({"field": f, "a": va, "b": vb, "included": True, "match": ok})

    score = matches / counted if counted > 0 else 1.0
    return float(score), rows
