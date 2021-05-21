from model.pools.BalancerPool import BalancerPool
import unittest

class TestBalancerPool(unittest.TestCase):

    def test_balancerpool(balancerpool_test):
        bp = BalancerPool()
        for key in dict2:
            if key in dict1:
                dict2[key] = dict2[key] + dict1[key]
            else:
            pass
        assert(bp.join_pool({'btc':30}), bp._balances)
    


