"""Sample size, power and minimum detectable effect for evals."""

from __future__ import annotations


def sample_size(
    baseline: float,
    lift: float,
    alpha: float = 0.05,
    power: float = 0.8,
    correlation: float = 0.0,
) -> int:
    """Number of questions needed to detect `lift` over `baseline` accuracy.

    `correlation` is how correlated the two models' per-question scores are.
    Higher correlation means a paired test needs fewer questions.
    """
    # TODO (Day 4)
    raise NotImplementedError


def power(
    baseline: float,
    lift: float,
    n_questions: int,
    alpha: float = 0.05,
    correlation: float = 0.0,
) -> float:
    """Chance of detecting `lift` with `n_questions` questions."""
    # TODO (Day 4)
    raise NotImplementedError


def min_detectable_effect(
    baseline: float,
    n_questions: int,
    alpha: float = 0.05,
    power: float = 0.8,
    correlation: float = 0.0,
) -> float:
    """Smallest lift this benchmark can reliably detect."""
    # TODO (Day 4)
    raise NotImplementedError
