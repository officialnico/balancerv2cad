from model.StableMath import StableMath
from decimal import *

        # self.tester('calculateInvariant', self.calculateInvariant(20,[23,23]), 46)
        # self.tester('calcBptInGivenExactTokensOut', self.calcBptInGivenExactTokensOut(2,[222,3112,311],[11,22,310],2,4), 2)
        # # assert self.calcBptOutGivenExactTokensIn(22,[2,3,4,20],[2,1,2,1000],3,4), 56
        # # assert self.calcInGivenOut(2,[222,3112,311],1,1,4), 0.000002756210410895  
        # self.tester('getTokenBalanceGivenInvariantAndAllOtherBalances', self.getTokenBalanceGivenInvariantAndAllOtherBalances(22, [2,3,4,20], 1, 2), 0.002573235526125192)


def test_calcBptInGivenExactTokensOut(stablemath_test):
   
    assert StableMath.calcBptInGivenExactTokensOut(
        Decimal(2),
        [Decimal(222),Decimal(3112),Decimal(311)],
        [Decimal(11),Decimal(22),Decimal(310)],
        Decimal(2),Decimal(4)
        ) == 2
   
def test_calcBptOutGivenExactTokensIn(stablemath_test):
    
    assert StableMath.calcBptOutGivenExactTokensIn(22,[2,3,4,20],[2,1,2,1000],3,4) == 56
   
   
# def test_calcDueTokenProtocolSwapFeeAmount(stablemath_test): 
#     ...
  
def test_calcInGivenOut(stablemath_test):
     
    assert StableMath.calcInGivenOut(2,[222,3112,311],1,1,4) == 0.000002756210410895
  
# def test_calcOutGivenIn(stablemath_test):
#     ...

# def test_calcTokenInGivenExactBptOut(stablemath_test):
#     ...
 
# def test__calcTokenOutGivenExactBptIn(stablemath_test):
#     ...
 
# def test_calcTokensOutGivenExactBptIn(stablemath_test):
#     ...
 
def test_calculateInvariant(stablemath_test):

    assert StableMath.calculateInvariant(20,[23,23]) == 46

  
# def test_getTokenBalanceGivenInvariantAndAllOtherBalances(stablemath_test):

#     assert StableMath.getTokenBalanceGivenInvariantAndAllOtherBalances(22, [2,3,4,20], 1, 2) == 0.002573235526125192

 