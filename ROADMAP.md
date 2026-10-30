# Roadmap (3–4 hours a day)

Each day: write the code, un-skip or add the tests, make them pass, commit.

## Week 1: core statistics

| Day | Goal | Files | Done when |
|---|---|---|---|
| 1 | Load data, mean, plain standard error, CI | `result.py` | `test_result.py` passes with skips removed |
| 2 | Simulator + clustered standard errors + coverage tests | `simulate.py`, `result.py` | Coverage ≈ 95% with clusters; naive CI shown to under-cover |
| 3 | Paired comparison of two models | `compare.py` | Difference, CI, p-value, summary tested |
| 4 | Sample size, power, minimum detectable effect | `power.py` | Matches a known formula / simulation |
| 5 | Repeated samples per question | `variance.py`, `result.py` | Variance split tested on simulated data |

## Week 2: your edge

| Day | Goal | Files | Done when |
|---|---|---|---|
| 6 | CUPED-style adjustment with question difficulty | `variance.py`, `compare.py` | Simulation shows a narrower CI with same coverage |
| 7 | Non-inferiority test | `compare.py` | Tested on simulated "cheaper model" cases |
| 8 | Multiple-comparison corrections | new `multiple.py` | Holm and Benjamini–Hochberg tested |
| 9–10 | Buffer: clean-up, docstrings, edge cases | all | CI green, ruff clean |

## Week 3: real data and write-up

| Day | Goal | Done when |
|---|---|---|
| 11–12 | Pull per-question leaderboard results (Hugging Face) | Clean CSVs for several models in `examples/` |
| 13 | Analysis notebook: how many close gaps are real? | Headline number + one chart |
| 14 | README headline, blog post draft | README updated, post in `docs/` |
| 15 | Optional: publish to PyPI | `pip install evalstats` works |
