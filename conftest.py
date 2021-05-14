from model.pools.stable.StableMath import StableMath
from model.pools.weighted.WeightedMath import WeightedMath
from model.pools.BalancerPoolToken import BalancerPoolToken
from model.pools.BasePool import BasePool

import pytest


@pytest.fixture()
def stablemath_test() -> None:
    yield StableMath

@pytest.fixture()
def weightedmath_test() -> None:
    yield WeightedMath

@pytest.fixture()
def basepool_test() -> None:
    yield BasePool

@pytest.fixture()
def balancer_pool_token_test() -> None:
    yield BalancerPoolToken

