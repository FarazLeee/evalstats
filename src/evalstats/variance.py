"""Variance helpers: repeated samples per question, and variance reduction."""

from __future__ import annotations

import pandas as pd


def split_variance(data: pd.DataFrame, score: str, question: str) -> dict[str, float]:
    """Split total variance into 'between questions' and 'within a question'.

    Within-question variance comes from the model's own randomness when it is
    sampled several times on the same question.
    """
    # TODO (Day 5)
    raise NotImplementedError


def cuped_adjust(y: pd.Series, x: pd.Series) -> pd.Series:
    """CUPED-style adjustment: y - theta * (x - mean(x)), with theta = cov(y, x) / var(x).

    For evals, x is a per-question covariate such as question difficulty
    (e.g. how other models did on that question).
    """
    # TODO (Day 6)
    raise NotImplementedError
