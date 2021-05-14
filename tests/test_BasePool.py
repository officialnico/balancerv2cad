from typing import List
from model.pools.BasePool import BasePool
from decimal import Decimal
import unittest
from model.vault.Vault import Vault



def test_get_vault(basepool_test):
    bp = basepool_test
    bp = BasePool(Vault(), 'foo', 'FOO', ['btc','bal'],Decimal(0.2),0)
    result = bp.get_vault()
    assert isinstance(result, object)

def test_get_pool_id(basepool_test):
    bp = BasePool(Vault(), 'foo', 'FOO', ['btc','bal'],Decimal(0.2),0)
    assert bp.get_pool_id() == 0

def test_get_total_tokens(basepool_test):
    bp = BasePool(Vault(), 'foo', 'FOO', ['btc','bal'],Decimal(0.2),0)
    assert bp.get_total_tokens() == 2

def test_get_swap_fee_percentage(basepool_test):
    bp = BasePool(Vault(), 'foo', 'FOO', ['btc','bal'],Decimal(0.2),0)
    fee = bp.get_swap_fee_percentage()
    assert fee == Decimal(0.23)

def test_set_swap_fee_percentage(selfbasepool_test):
    bp = BasePool(Vault(), 'foo', 'FOO', ['btc','bal'],Decimal(0.2),0)
    fee = bp.set_swap_fee_percentage(Decimal(0.24))
    assert fee == Decimal(0.24)





