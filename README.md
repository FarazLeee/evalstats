# evalstats

**Is the gap between two models on a benchmark real, or just noise?**

`evalstats` adds error bars, paired comparisons and power analysis to LLM evaluations, plus
methods borrowed from A/B testing (CUPED-style variance reduction, non-inferiority tests) that
most eval reports skip.

> 🚧 Work in progress. Headline result and chart coming soon.

## Headline result

_To be added: what share of close leaderboard gaps are not statistically meaningful._

## Install

```bash
git clone https://github.com/<your-username>/evalstats.git
cd evalstats
pip install -e ".[dev]"
```

## Quick example

```python
from evalstats import EvalResult, compare, sample_size

a = EvalResult.from_csv("model_a.csv", score="correct", cluster="passage_id")
b = EvalResult.from_csv("model_b.csv", score="correct", cluster="passage_id")

print(a.ci())  # 0.712 (0.689 – 0.735)
print(compare(a, b).summary())  # difference, CI, p-value
compare(a, b).noninferior(margin=0.01)
sample_size(baseline=0.70, lift=0.02)
```

## What's included

| Feature | Status |
|---|---|
| Confidence interval for one model's score | ⬜ |
| Clustered standard errors (related questions) | ⬜ |
| Paired comparison of two models | ⬜ |
| Sample size, power, minimum detectable effect | ⬜ |
| Repeated samples per question | ⬜ |
| CUPED-style variance reduction | ⬜ |
| Non-inferiority tests | ⬜ |
| Multiple-comparison corrections | ⬜ |

## How correctness is checked

Simulation tests generate fake eval results with a known true accuracy and confirm that 95%
intervals contain the truth about 95% of the time. See `tests/test_coverage.py`.

## References

- Evan Miller, [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) (2024)
- Deng et al., Improving the Sensitivity of Online Controlled Experiments by Utilizing
  Pre-Experiment Data (CUPED, 2013)

## License

MIT
