from typing import List
from model.pools.stable.StableMath import StableMath
from decimal import Decimal
import unittest
# self.tester('calculateInvariant', self.calculateInvariant(20,[23,23]), 46)
# self.tester('calc_bpt_in_given_exact_tokens_out', self.calc_bpt_in_given_exact_tokens_out(2,[222,3112,311],[11,22,310],2,4), 2)
# # assert self.calc_bpt_out_given_exact_tokens_in(22,[2,3,4,20],[2,1,2,1000],3,4), 56
# # assert self.calcInGivenOut(2,[222,3112,311],1,1,4), 0.000002756210410895
# self.tester('getTokenBalanceGivenInvariantAndAllOtherBalances', self.getTokenBalanceGivenInvariantAndAllOtherBalances(22, [2,3,4,20], 1, 2), 0.002573235526125192)



class TestStableMath(unittest.TestCase):


    # def test_calc_bpt_in_given_exact_tokens_out(stablemath_test):

    #     assert StableMath.calc_bpt_in_given_exact_tokens_out(
    #         Decimal(2),
    #         [Decimal(222),Decimal(3112),Decimal(311)],
    #         [Decimal(11),Decimal(22),Decimal(310)],
    #         Decimal(2),Decimal(4)
    #         ) == 2

    def test_calcBptOutGivenExactTokensIn(stablemath_test):
        #TODO assert StableMath.calc_bpt_out_given_exact_tokens_in(22,[2,3,4,20],[2,1,2,1000],3,4) == 56.

        amp = Decimal(22)
        balances = [Decimal(2), Decimal(3),Decimal(4), Decimal(20)]
        amountsIn = [Decimal(2), Decimal(1), Decimal(2), Decimal(1000)]
        bptTotalsupply = Decimal(10)
        swapFee = Decimal(2)
        swapFeePercentage = Decimal(.04)
        result = StableMath.calcBptOutGivenExactTokensIn(amp, balances, amountsIn,bptTotalsupply, swapFee,swapFeePercentage)
        assert isinstance(result, Decimal)

    def test_calcInGivenOut(stablemath_test):
       #TODO assert StableMath.calcInGivenOut(2,[222,3112,311],1,1,4) == 0.000002756210410895
        amp = Decimal(100)
        balances = [Decimal(10), Decimal(12), Decimal(14)]
        tokenIndexIn = 0
        tokenIndexOut = 1
        tokenAmountOut = Decimal(1)
        result = StableMath.calcInGivenOut(amp, balances, tokenIndexIn, tokenIndexOut, tokenAmountOut)
        assert isinstance(result, Decimal)

    def test_calcOutGivenIn(stablemath_test):
        #    def calcOutGivenIn(amplificationParameter: Decimal, balances: list[Decimal], tokenIndexIn: int, tokenIndexOut: int, tokenAmountIn: Decimal):
        amp = Decimal(10)
        balances = [Decimal(10), Decimal(11), Decimal(12)]
        tokenIndexIn = 0
        tokenIndexOut = 1
        tokenAmountIn = Decimal(1)
        result = StableMath.calcOutGivenIn(amp, balances, tokenIndexIn, tokenIndexOut, tokenAmountIn)
        assert isinstance(result, Decimal)

    def test_calcTokenInGivenExactBptOut(stablemath_test):
        amp = Decimal(100)
        balances = [Decimal(10),Decimal(11)]
        amountsOut = [Decimal(5),Decimal(6)]
        bptTotalSupply = Decimal(100)
        protocolSwapFeePercentage = Decimal(0.1)
        result = StableMath.calcBptInGivenExactTokensOut(amp, 
                                                balances,
                                                amountsOut,
                                                bptTotalSupply,
                                                protocolSwapFeePercentage)
        assert isinstance(result, Decimal)


    def test_calcTokenOutGivenExactBptIn(stablemath_test):
        balances = [Decimal(10),Decimal(11)]
        bptAmountIn = Decimal(10)
        bptTotalSupply =Decimal(2)
        result = StableMath.calcTokensOutGivenExactBptIn(balances,bptAmountIn, bptTotalSupply)
        assert isinstance(result, list)

    def test_calcTokensOutGivenExactBptIn(stablemath_test):
        balances = [Decimal(10),Decimal(11)]
        bptAmountIn = Decimal(10)
        bptTotalSupply =Decimal(2)
        result = StableMath.calcTokensOutGivenExactBptIn(balances,bptAmountIn,bptTotalSupply)
        assert isinstance(result, list)
    def test_calculateInvariantTwoTokens(self):
        amp = Decimal(100)
        balances = [10,12]
        result =  StableMath.calculateInvariant(amp, balances)
        assert isinstance(result, Decimal)

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


