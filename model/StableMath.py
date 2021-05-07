from decimal import Decimal
from attr import dataclass
from math import ceil, floor


@dataclass
class BalancerMathResult:
    result: Decimal
    fee: Decimal

class StableMath:
# This function calculates the balance of a given token (tokenIndex)
# given all the other balances and the invariant


# -------------------------------------


    def calcBptInGivenExactTokensOut(amplificationParameter: int, balances: list, amountsOut: list, bptTotalSupply: int, swapFee: int) -> int:
        return 0
    
    def calcBptOutGivenExactTokensIn(amplificationParameter: int, balances: list, amountsIn: list, bptTotalSupply: int, swapFee: int):
        ...
    
    def calcDueTokenProtocolSwapFeeAmount(amplificationParameter: int, balances: list, lastIvariant: int, bptTotalSupply: int, swapFee: int):
        ...

    def calcInGivenOut(amplificationParameter: int, balances: list, tokenIndexIn: int, tokenIndexOut: int, tokenAmountOut: int):
        ...

    def calcOutGivenIn():
        ...

    def calcTokenInGivenExactBptOut():
        ...

    def calcTokensOutGivenExactBptIn():
        ...

    def calcTokenOutGivenExactBptIn():
        ...


    # ------------------------------------

    def getTokenBalanceGivenInvariantAndAllOtherBalances(amplificationParameter: int, balances: list, invariant: int, tokenIndex: int) -> int:
        amplificationParameter = Decimal(amplificationParameter)
        

    def calculateInvariant(amplificationParameter: int, balances: list) -> int:
        bal_sum = 0
        for bal in balances:
            bal_sum += bal
        num_tokens = len(balances)
        if(bal_sum==0):
            return 0
        prevInvariant = 0
        invariant = bal_sum
        ampTimesTotal = amplificationParameter*num_tokens
        for i in range(255):
            P_D = num_tokens*balances[0]
            for j in range(1, num_tokens):
                P_D = ceil(((P_D*balances[j])*num_tokens)/invariant)
            prevInvariant = invariant

            invariant = ceil(((num_tokens*invariant)*invariant + (ampTimesTotal*bal_sum)*P_D) / ((num_tokens + 1)*invariant + (ampTimesTotal - 1)*P_D))
            if(invariant > prevInvariant):
                if(invariant - prevInvariant <= 1):
                    break
            elif(prevInvariant - invariant <= 1):
                break
        return invariant

    # ----------------------Test------------------------
    def tester(title, result, expected):
        res = result == expected
        if(not res): print(title, res, '| Result:', result, 'Expected:', expected, 'diff->', abs(result - expected))
        else:  print(title, res)

#     def test():
#         self.tester('calculateInvariant', self.calculateInvariant(20,[23,23]), 46)
#         self.tester('calcBptInGivenExactTokensOut', self.calcBptInGivenExactTokensOut(2,[222,3112,311],[11,22,310],2,4), 2)
#         # assert self.calcBptOutGivenExactTokensIn(22,[2,3,4,20],[2,1,2,1000],3,4), 56
#         # assert self.calcInGivenOut(2,[222,3112,311],1,1,4), 0.000002756210410895  
#         self.tester('getTokenBalanceGivenInvariantAndAllOtherBalances', self.getTokenBalanceGivenInvariantAndAllOtherBalances(22, [2,3,4,20], 1, 2), 0.002573235526125192)

# if __name__=='__main__':
#     stab = StableMath()
#     stab.test()