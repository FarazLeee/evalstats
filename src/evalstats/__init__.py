"""evalstats: statistics for LLM evaluations."""

from evalstats.compare import Comparison, compare
from evalstats.power import min_detectable_effect, power, sample_size
from evalstats.result import EvalResult

__all__ = [
    "Comparison",
    "EvalResult",
    "compare",
    "min_detectable_effect",
    "power",
    "sample_size",
]

__version__ = "0.0.1"
