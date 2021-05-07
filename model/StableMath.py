from decimal import *
from attr import dataclass
from math import ceil, floor
from model.util import *

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

    def getTokenBalanceGivenInvariantAndAllOtherBalances(amplificationParameter: Decimal, balances: list[Decimal], invariant: Decimal, tokenIndex: int) -> Decimal:
        getcontext().prec = 18
        
        ampTimesTotal = amplificationParameter * len(balances)
        bal_sum = Decimal(sum(balances))

        P_D = len(balances) * balances[0]
        for i in range(1, len(balances)):
            P_D = (P_D*balances[i]*len(balances))/invariant

        bal_sum -= balances[tokenIndex]

        c = invariant*invariant/ampTimesTotal
        c = divUp(mulUp(c, balances[tokenIndex]), P_D)

        print(type(bal_sum),type(invariant),type(ampTimesTotal))
        b = bal_sum + divDown(invariant, ampTimesTotal)

        prevTokenbalance = 0
        tokenBalance = divUp((invariant*invariant+c), (invariant+b))

        for i in range(255):
            prevTokenbalance = tokenBalance
            tokenBalance = divUp((mulUp(tokenBalance,tokenBalance) + c),((tokenBalance*2)+b-invariant))
            if(tokenBalance > prevTokenbalance):
                if(tokenBalance-prevTokenbalance <= 1):
                    break
            elif(prevTokenbalance-tokenBalance <= 1):
                break

        return tokenBalance

    def calculateInvariant(amplificationParameter: Decimal, balances: list[Decimal]) -> int:
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

