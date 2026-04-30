"""Component C: two-level entity deviation similarity."""

from __future__ import annotations

from typing import Any, Iterable

import numpy as np


def _population_mean_entity_totals(population: list[dict[str, int]], entity_keys: Iterable[str]) -> dict[str, float]:
    keys = list(entity_keys)
    out: dict[str, float] = {}
    for k in keys:
        vals = [float(p.get(k, 0)) for p in population]
        out[k] = float(np.mean(vals)) if vals else 0.0
    return out


def entity_deviation_level1(entity_counts_a: dict[str, int], entity_counts_b: dict[str, int], population_entity_totals: list[dict[str, int]], entity_keys: Iterable[str]) -> tuple[float, list[dict[str, Any]]]:
    """Component C/L1: compare study-wide deviation magnitudes from population means."""
    keys = list(entity_keys)
    mu = _population_mean_entity_totals(population_entity_totals, keys)
    num = 0.0
    den = 0.0
    rows = []
    for k in keys:
        c_a = float(entity_counts_a.get(k, 0))
        c_b = float(entity_counts_b.get(k, 0))
        m = mu[k]
        d_a, d_b = c_a - m, c_b - m
        denom = max(abs(d_a), abs(d_b), 1.0)
        sim_e = 1.0 - min(abs(d_a - d_b) / denom, 1.0)
        w_e = max(abs(d_a), abs(d_b), 0.1)
        num += sim_e * w_e
        den += w_e
        rows.append({
            "entity": k,
            "mu": m,
            "count_a": c_a,
            "count_b": c_b,
            "delta_a": d_a,
            "delta_b": d_b,
            "per_entity_sim": sim_e,
            "weight": w_e,
        })
    score = num / den if den > 0 else 1.0
    return score, rows


def _population_mean_section_per_entity(population: list[dict[str, np.ndarray]], entity_keys: Iterable[str], n_sections: int) -> dict[str, np.ndarray]:
    keys = list(entity_keys)
    out: dict[str, np.ndarray] = {}
    for k in keys:
        stacks = []
        for p in population:
            arr = p.get(k)
            if arr is not None:
                a = np.asarray(arr, dtype=float).ravel()
                if a.size == n_sections:
                    stacks.append(a)
        if stacks:
            out[k] = np.mean(np.stack(stacks, axis=0), axis=0)
        else:
            out[k] = np.zeros(n_sections, dtype=float)
    return out


def entity_deviation_level2(
    entity_counts_a: dict[str, int],
    entity_counts_b: dict[str, int],
    entity_by_section_a: dict[str, np.ndarray],
    entity_by_section_b: dict[str, np.ndarray],
    population_section_per_entity: list[dict[str, np.ndarray]],
    entity_keys: Iterable[str],
    step_threshold: float = 0.5,
) -> tuple[float, list[dict[str, Any]]]:
    """Component C/L2: compare section-level deviation directions on salient entities."""
    keys = list(entity_keys)
    if not keys or not population_section_per_entity:
        return 1.0, []

    sample = next(iter(entity_by_section_a.values()), None)
    if sample is None:
        return 1.0, []
    n_sections = int(np.asarray(sample).size)
    mu_tot = _population_mean_entity_totals(
        [{k: float(arr.sum()) for k, arr in p.items()} for p in population_section_per_entity],
        keys,
    )
    mu_sec = _population_mean_section_per_entity(population_section_per_entity, keys, n_sections)

    matches = 0
    compared = 0
    detail_rows: list[dict[str, Any]] = []
    for k in keys:
        c_a = float(entity_counts_a.get(k, 0))
        c_b = float(entity_counts_b.get(k, 0))
        m = mu_tot[k]
        if abs(c_a - m) < step_threshold and abs(c_b - m) < step_threshold:
            continue

        sa = entity_by_section_a.get(k)
        sb = entity_by_section_b.get(k)
        if sa is None or sb is None:
            continue
        sa = np.asarray(sa, dtype=float).ravel()
        sb = np.asarray(sb, dtype=float).ravel()
        mvec = mu_sec.get(k, np.zeros(n_sections))
        if sa.size != n_sections or sb.size != n_sections:
            continue

        for j in range(n_sections):
            d_a = sa[j] - mvec[j]
            d_b = sb[j] - mvec[j]
            if abs(d_a) < step_threshold and abs(d_b) < step_threshold:
                continue
            compared += 1
            if np.sign(d_a) == np.sign(d_b):
                matches += 1
            detail_rows.append({
                "entity": k,
                "section_index": j,
                "delta_a_section": d_a,
                "delta_b_section": d_b,
                "agree_sign": bool(np.sign(d_a) == np.sign(d_b)),
            })

    score = matches / compared if compared > 0 else 1.0
    return float(score), detail_rows


def entity_deviation_combined(level1: float, level2: float, w1: float = 0.7, w2: float = 0.3) -> float:
    """Blend Level 1 and Level 2 deviation scores."""
    return w1 * level1 + w2 * level2
