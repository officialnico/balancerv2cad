from decimal import Decimal
from model.pools.stable.StablePool import StablePool
import unittest


class TestStablePool(unittest.TestCase):

    def test_balancerpool(stablepool_test):
        ...
    
    def test_swap_given_in(stablepool_test):
        POOL_SWAP_FEE_PERCENTAGE = Decimal(0.01)
        sp = StablePool()
        balances = {'uni': Decimal(1), 'weth': Decimal(0.9)}
        sp.join_pool(balances)
        amount = Decimal(0.1)
        amount_with_fees = amount*(POOL_SWAP_FEE_PERCENTAGE + Decimal(1))/Decimal(1)
        expected = Decimal(100986343323831144)/Decimal(1e18)
        result  = sp.swap('weth', 'uni', amount_with_fees, given_in=True)
        assert sp._balances['uni'] == expected



    