"""Simulation checks: do 95% intervals contain the true value about 95% of the time?

These are the tests that prove the library is correct, not just that it runs.
"""

import pytest


@pytest.mark.skip(reason="Day 2: implement simulate_results and clustered standard errors")
def test_ci_coverage_without_clusters():
    # Simulate many benchmarks with known accuracy, build a CI for each,
    # and check the share that contains the truth is close to 0.95.
    ...


@pytest.mark.skip(reason="Day 2: show naive CIs under-cover when questions are clustered")
def test_clustered_ci_coverage(): ...
