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

    # Flow of calculations:
    #  amountsTokenOut -> amountsOutProportional ->
    #  amountOutPercentageExcess -> amountOutBeforeFee -> newInvariant -> amountBPTIn
    
    def calcBptInGivenExactTokensOut(amplificationParameter: Decimal, balances: list[Decimal], amountsOut: list[Decimal], bptTotalSupply: Decimal, swapFee: Decimal) -> int:
        return 0
    
    # Flow of calculations:
    #  amountsTokenIn -> amountsInProportional ->
    #  amountsInPercentageExcess -> amountsInAfterFee -> newInvariant -> amountBPTOut
    #  TODO: remove equations below and save them to Notion documentation
    #  amountInPercentageExcess = 1 - amountInProportional/amountIn (if amountIn>amountInProportional)
    #  amountInAfterFee = amountIn * (1 - swapFeePercentage * amountInPercentageExcess)
    #  amountInAfterFee = amountIn - fee amount
    #  fee amount = (amountIn - amountInProportional) * swapFeePercentage
    #  amountInAfterFee = amountIn - (amountIn - amountInProportional) * swapFeePercentage
    #  amountInAfterFee = amountIn * (1 - (1 - amountInProportional/amountIn) * swapFeePercentage)
    #  amountInAfterFee = amountIn * (1 - amountInPercentageExcess * swapFeePercentage)
    
    def calcBptOutGivenExactTokensIn(amplificationParameter: Decimal, balances: list[Decimal], amountsIn: list[Decimal], bptTotalSupply: Decimal, swapFee: Decimal):
        ...
    
    def calcDueTokenProtocolSwapFeeAmount(amplificationParameter: Decimal, balances: list[Decimal], lastIvariant: Decimal, bptTotalSupply: Decimal, swapFee: Decimal):
        # /**************************************************************************************************************
        # // oneTokenSwapFee - polynomial equation to solve                                                            //
        # // af = fee amount to calculate in one token                                                                 //
        # // bf = balance of fee token                                                                                 //
        # // f = bf - af (finalBalanceFeeToken)                                                                        //
        # // D = old invariant                                            D                     D^(n+1)                //
        # // A = amplification coefficient               f^2 + ( S - ----------  - D) * f -  ------------- = 0         //
        # // n = number of tokens                                    (A * n^n)               A * n^2n * P              //
        # // S = sum of final balances but f                                                                           //
        # // P = product of final balances but f                                                                       //
        # *******
        ...

    def calcInGivenOut(amplificationParameter: Decimal, balances: list[Decimal], tokenIndexIn: int, tokenIndexOut: int, tokenAmountOut: Decimal):
        
        # /**************************************************************************************************************
        # // inGivenOut token x for y - polynomial equation to solve                                                   //
        # // ax = amount in to calculate                                                                               //
        # // bx = balance token in                                                                                     //
        # // x = bx + ax (finalBalanceIn)                                                                              //
        # // D = invariant                                                D                     D^(n+1)                //
        # // A = amplification coefficient               x^2 + ( S - ----------  - D) * x -  ------------- = 0         //
        # // n = number of tokens                                     (A * n^n)               A * n^2n * P             //
        # // S = sum of final balances but x                                                                           //
        # // P = product of final balances but x                                                                       //
        # **************************************************************************************************************/



        
    def calcOutGivenIn(amplificationParameter: Decimal, balances: list[Decimal], tokenIndexIn: int, tokenIndexOut: int, tokenAmountIn: Decimal):
        
        # /**************************************************************************************************************
        # // outGivenIn token x for y - polynomial equation to solve                                                   //
        # // ay = amount out to calculate                                                                              //
        # // by = balance token out                                                                                    //
        # // y = by - ay (finalBalanceOut)                                                                             //
        # // D = invariant                                               D                     D^(n+1)                 //
        # // A = amplification coefficient               y^2 + ( S - ----------  - D) * y -  ------------- = 0         //
        # // n = number of tokens                                    (A * n^n)               A * n^2n * P              //
        # // S = sum of final balances but y                                                                           //
        # // P = product of final balances but y                                                                       //
        # **************************************************************************************************************/

        ...

    # Flow of calculations:
    #  amountBPTOut -> newInvariant -> (amountInProportional, amountInAfterFee) ->
    #  amountInPercentageExcess -> amountIn
        
    def calcTokenInGivenExactBptOut():
        ...

    def calcTokensOutGivenExactBptIn():
        
        # /**********************************************************************************************
        # // exactBPTInForTokensOut                                                                    //
        # // (per token)                                                                               //
        # // aO = tokenAmountOut             /        bptIn         \                                  //
        # // b = tokenBalance      a0 = b * | ---------------------  |                                 //
        # // bptIn = bptAmountIn             \     bptTotalSupply    /                                 //
        # // bpt = bptTotalSupply                                                                      //
        # **********************************************************************************************/
        ...
        
    # Flow of calculations:
    #  amountBPTin -> newInvariant -> (amountOutProportional, amountOutBeforeFee) ->
    #  amountOutPercentageExcess -> amountOut

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
        
        # /**********************************************************************************************
        # // invariant                                                                                 //
        # // D = invariant                                                  D^(n+1)                    //
        # // A = amplification coefficient      A  n^n S + D = A D n^n + -----------                   //
        # // S = sum of balances                                             n^n P                     //
        # // P = product of balances                                                                   //
        # // n = number of tokens                                                                      //
        # *********x************************************************************************************/
        
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

