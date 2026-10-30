"""Comparing two models on the same benchmark."""

from __future__ import annotations

from evalstats.result import ConfidenceInterval, EvalResult


class Comparison:
    """Paired comparison of model A vs model B on the same questions."""

    def __init__(
        self,
        a: EvalResult,
        b: EvalResult,
        covariate: str | None = None,
    ) -> None:
        # TODO (Day 3): align the two results on question_id and keep only shared questions.
        self.a = a
        self.b = b
        self.covariate = covariate

    def difference(self) -> float:
        """Mean score of B minus mean score of A."""
        # TODO (Day 3)
        raise NotImplementedError

    def ci(self, level: float = 0.95) -> ConfidenceInterval:
        """Confidence interval for the difference, using the paired standard error."""
        # TODO (Day 3; Day 6 adds the CUPED-style adjustment when covariate is set)
        raise NotImplementedError

    def p_value(self) -> float:
        """Two-sided p-value for 'no difference'."""
        # TODO (Day 3)
        raise NotImplementedError

    def noninferior(self, margin: float, level: float = 0.95) -> bool:
        """True if B is no worse than A by more than `margin`."""
        # TODO (Day 7)
        raise NotImplementedError

    def summary(self) -> str:
        """Plain-language summary of the comparison."""
        # TODO (Day 3)
        raise NotImplementedError


def compare(a: EvalResult, b: EvalResult, covariate: str | None = None) -> Comparison:
    """Shortcut for Comparison(a, b, covariate)."""
    return Comparison(a, b, covariate=covariate)
