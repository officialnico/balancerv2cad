from decimal import Decimal
from attr import dataclass
from math import ceil, floor


@dataclass
class BalancerMathResult:
    result: Decimal
    fee: Decimal

class StableMath:

# -------------------------------------


    def calcBptInGivenExactTokensOut(amplificationParameter: Decimal, balances: list[Decimal], amountsOut: list[Decimal], bptTotalSupply: Decimal, swapFee: Decimal) -> int:
        return 0
    
    def calcBptOutGivenExactTokensIn(amplificationParameter: Decimal, balances: list[Decimal], amountsIn: list[Decimal], bptTotalSupply: Decimal, swapFee: Decimal):
        ...
    
    def calcDueTokenProtocolSwapFeeAmount(amplificationParameter: Decimal, balances: list[Decimal], lastIvariant: Decimal, bptTotalSupply: Decimal, swapFee: Decimal):
        ...

    def calcInGivenOut(amplificationParameter: Decimal, balances: list[Decimal], tokenIndexIn: int, tokenIndexOut: int, tokenAmountOut: Decimal):
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

