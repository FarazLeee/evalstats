import evalstats


def test_package_imports():
    assert evalstats.__version__
    assert hasattr(evalstats, "EvalResult")
    assert hasattr(evalstats, "compare")
