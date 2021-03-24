---
created: 2021-03-11
tag: pytest
---
# Pytest's equivalent of unittest's assertAlmostEqual

Looking to compare floats in pytest tests? Try `pytest.approx()`. It's similar to but
more flexible than unittest's `assertAlmostEqual()`.

The [documentation for pytest.approx()](https://docs.pytest.org/en/4.6.x/reference.html#pytest-approx)
includes a handy section covering the differences between `approx()` and various similar
tools, including `assertAlmostEqual()` and `isclose` from both `math` and `numpy`.