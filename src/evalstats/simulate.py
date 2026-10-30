"""Fake eval results with a known true accuracy, used to check the methods work."""

from __future__ import annotations

import pandas as pd


def simulate_results(
    n_questions: int,
    true_accuracy: float,
    n_clusters: int | None = None,
    cluster_sd: float = 0.0,
    samples_per_question: int = 1,
    seed: int | None = None,
) -> pd.DataFrame:
    """Generate one model's results.

    Returns columns question_id, cluster_id (if clustered), sample, score.
    Clusters shift accuracy up or down for all their questions, which is what
    makes naive error bars too narrow.
    """
    # TODO (Day 2)
    raise NotImplementedError
