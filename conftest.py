from model.pools.stable.StableMath import StableMath
from model.pools.weighted.WeightedMath import WeightedMath
from model.pools.BalancerPoolToken import BalancerPoolToken
from model.pools.BasePool import BasePool
from model.vault.Vault import Vault

from decimal import Decimal
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
    basepool = BasePool(vault, 'foo', 'FOO', {'btc':20,'eth':200},Decimal(0.2),0,0)
    yield basepool

def balancerpooltoken_test() -> None:
    v = Vault()
    handler = BalancerPoolToken(v, 'test', 'TST', ['bal','btc'],Decimal(0.23), 0)
    yield handler

