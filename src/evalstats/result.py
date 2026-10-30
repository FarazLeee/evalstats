"""One model's results on one benchmark, and error bars for its score."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class ConfidenceInterval:
    """A point estimate with lower and upper bounds."""

    estimate: float
    lower: float
    upper: float
    level: float = 0.95

    def __str__(self) -> str:
        return f"{self.estimate:.3f} ({self.lower:.3f} – {self.upper:.3f})"


class EvalResult:
    """Per-question scores for one model on one benchmark.

    Expected data: one row per (question, sample). Columns:
      - question_id: identifies the question
      - score:       0/1 for correct/incorrect, or any number for graded scores
      - cluster_id:  optional, groups related questions (e.g. same passage)
    """

    def __init__(
        self,
        data: pd.DataFrame,
        score: str = "score",
        question: str = "question_id",
        cluster: str | None = None,
    ) -> None:
        # TODO (Day 1): validate that the columns exist and scores are numeric.
        self.data = data
        self.score_col = score
        self.question_col = question
        self.cluster_col = cluster

    @classmethod
    def from_csv(cls, path: str, **kwargs) -> EvalResult:
        """Load results from a CSV file."""
        # TODO (Day 1)
        raise NotImplementedError

    @property
    def n_questions(self) -> int:
        """Number of distinct questions."""
        # TODO (Day 1)
        raise NotImplementedError

    def mean(self) -> float:
        """Average score across questions (average samples within a question first)."""
        # TODO (Day 1)
        raise NotImplementedError

    def standard_error(self) -> float:
        """Standard error of the mean.

        Plain version when there are no clusters; clustered version when
        cluster_col is set (Day 2).
        """
        # TODO (Day 1: plain, Day 2: clustered)
        raise NotImplementedError

    def ci(self, level: float = 0.95) -> ConfidenceInterval:
        """Confidence interval for the mean score."""
        # TODO (Day 1)
        raise NotImplementedError
