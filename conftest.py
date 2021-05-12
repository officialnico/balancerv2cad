from model.pools.stable.StableMath import StableMath
from model.pools.weighted.WeightedMath import WeightedMath

import pytest

@pytest.fixture()
def stablemath_test() -> None:
    yield StableMath


@pytest.fixture()
def weightedmath_test() -> None:
    yield WeightedMath
