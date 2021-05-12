from model.pools.stable.StableMath import StableMath
from decimal import *
import unittest
# self.tester('calculateInvariant', self.calculateInvariant(20,[23,23]), 46)
# self.tester('calcBptInGivenExactTokensOut', self.calcBptInGivenExactTokensOut(2,[222,3112,311],[11,22,310],2,4), 2)
# # assert self.calcBptOutGivenExactTokensIn(22,[2,3,4,20],[2,1,2,1000],3,4), 56
# # assert self.calcInGivenOut(2,[222,3112,311],1,1,4), 0.000002756210410895
# self.tester('getTokenBalanceGivenInvariantAndAllOtherBalances', self.getTokenBalanceGivenInvariantAndAllOtherBalances(22, [2,3,4,20], 1, 2), 0.002573235526125192)



class TestStableMath(unittest.TestCase):



    def test_calcBptOutGivenExactTokensIn(stablemath_test):
        #TODO assert StableMath.calcBptOutGivenExactTokensIn(22,[2,3,4,20],[2,1,2,1000],3,4) == 56.
        result = StableMath.calcBptOutGivenExactTokensIn(22,[2,3,4,20],[2,1,2,1000],3,4)
        assert isinstance(result, Decimal)

    def test_calcInGivenOut(stablemath_test):
       #TODO assert StableMath.calcInGivenOut(2,[222,3112,311],1,1,4) == 0.000002756210410895
        result = StableMath.calcInGivenOut(100,[10,12,14],0,1,1)
        assert isinstance(result, Decimal)

    def test_calcOutGivenIn(stablemath_test):
        #    def calcOutGivenIn(amplificationParameter: Decimal, balances: list[Decimal], tokenIndexIn: int, tokenIndexOut: int, tokenAmountIn: Decimal):
        result = StableMath.calcOutGivenIn(10, [10,11,12],0,1,1)
        assert isinstance(result, Decimal)

    def test_calcTokenInGivenExactBptOut(stablemath_test):
        ...

    def test_calcTokenOutGivenExactBptIn(stablemath_test):
        ...

    def test_calcTokensOutGivenExactBptIn(stablemath_test):
        ...

    def test_calculateInvariant(self):
        assert StableMath.calculateInvariant(20,[23,23]) == 46

    #TODO give critical results
    def test_getTokenBalanceGivenInvariantAndAllOtherBalances(self):

        # assert StableMath.getTokenBalanceGivenInvariantAndAllOtherBalances(22, [2,3,4,20], 1, 2) == 0.002573235526125192

        # self.assertAlmostEqual(
        #     StableMath.getTokenBalanceGivenInvariantAndAllOtherBalances(
        #         Decimal(22),
        #         [Decimal(2),Decimal(3),Decimal(4),Decimal(20)],
        #         Decimal(1),
        #         2), Decimal(0.00067593918100831), 3)
        #print(TestCase.assertAlmostEqual(1,1.00000000000001,3))

        assert isinstance(StableMath.getTokenBalanceGivenInvariantAndAllOtherBalances(
            Decimal(22),
            [Decimal(2),Decimal(3),Decimal(4),Decimal(20)],
            Decimal(1),
            2), Decimal)


    # def test_calcBptInGivenExactTokensOut(stablemath_test):

    #     assert StableMath.calcBptInGivenExactTokensOut(
    #         Decimal(2),
    #         [Decimal(222),Decimal(3112),Decimal(311)],
    #         [Decimal(11),Decimal(22),Decimal(310)],
    #         Decimal(2),Decimal(4)
    #         ) == 2