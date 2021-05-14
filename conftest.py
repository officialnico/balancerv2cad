from model.pools.stable.StableMath import StableMath
from model.pools.weighted.WeightedMath import WeightedMath
from model.pools.BalancerPoolToken import BalancerPoolToken
from model.pools.BasePool import BasePool
from model.vault.Vault import Vault


import pytest


@pytest.fixture()
def stablemath_test() -> None:
    yield StableMath

@pytest.fixture()
def weightedmath_test() -> None:
    yield WeightedMath

@pytest.fixture()
def basepool_test() -> None:
    vault = Vault()
    basepool = BasePool(vault, 'foo', 'FOO', {'btc','eth':200},Decimal(0.2),0,0)
    yield basepool

@pytest.fixture()
def balancer_pool_token_test() -> None:
    yield BalancerPoolToken


