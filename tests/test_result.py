"""Tests for EvalResult. Remove the skip marks as you implement each piece."""

import pandas as pd
import pytest

from evalstats import EvalResult


@pytest.fixture
def simple_data():
    return pd.DataFrame({"question_id": [1, 2, 3, 4], "score": [1, 0, 1, 1]})


@pytest.mark.skip(reason="Day 1: implement EvalResult.mean")
def test_mean(simple_data):
    assert EvalResult(simple_data).mean() == pytest.approx(0.75)


@pytest.mark.skip(reason="Day 1: implement EvalResult.n_questions")
def test_n_questions(simple_data):
    assert EvalResult(simple_data).n_questions == 4


@pytest.mark.skip(reason="Day 1: implement EvalResult.ci")
def test_ci_contains_mean(simple_data):
    ci = EvalResult(simple_data).ci()
    assert ci.lower <= ci.estimate <= ci.upper
