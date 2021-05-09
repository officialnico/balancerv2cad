from decimal import *
from attr import dataclass
from math import ceil, floor
from util import *

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

    def calcBptOutGivenExactTokensIn(amplificationParameter: Decimal, balances: list[Decimal], amountsIn: list[Decimal], bptTotalSupply: Decimal, swapFee: Decimal, swapFeePercentage: Decimal):
        # get current invariant
        currentInvariant = calculateInvariant(amplificationParameter, balances)

        sumBalances = Decimal(0)
        for i in range(len(balances)):
            sumBalances += i

        # Calculate the weighted balance ratio without considering fees
        tokenBalanceRatiosWithoutFee = []
        weightedBalanceRatio = 0
        for i in range(len(balances)):
            currentWeight = divDown(balances[i], sumBalances)
            tokenBalanceRatiosWithoutFee[i] = balances[i] + divDown(amountsIn[i], balances[i])
            weightedBalanceRatio = weightedBalanceRatio + mulDown(tokenBalanceRatiosWithoutFee[i], currentWeight)

        tokenBalancePercentageExcess = Decimal(0)
        newBalances = []
        for i in range(len(balances)):
            if weightedBalanceRatio >= tokenBalanceRatiosWithoutFee[i]:
                tokenBalancePercentageExcess = Decimal(0)
            else:
                tokenBalancePercentageExcess = tokenBalanceRatiosWithoutFee[i] - divUp(weightedBalanceRatio, (tokenBalanceRatiosWithoutFee[i])) # TODO omitted subtracting ONE from token without fee

            swapFeeExcess = mulUp(swapFeePercentage, tokenBalancePercentageExcess)
            amountInAfterFee = mulDown(amountsIn[i], complement(swapFeeExcess))
            newBalances[i] = balances[i] + amountInAfterFee

        # get new invariant, taking swap fees into account
        newInvariant = calculateInvariant(amplificationParameter, newBalances)

        # return amountBPTOut
        return mulDown(bptTotalSupply, divDown(newInvariant, currentInvariant)) # TODO omitted subtracting ONE from currentInvariant



    def calcDueTokenProtocolSwapFeeAmount(amplificationParameter: Decimal, balances: list[Decimal], lastIvariant: Decimal, tokenIndex: int, protocolSwapFeePercentage: Decimal):
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
        finalBalanceFeeToken = getTokenBalanceGivenInvariantAndAllOtherBalances(
            amplificationParameter,
            balances,
            lastInvariant,
            tokenIndex)

        if(balances[tokenIndex] > finalBalanceFeeToken):
            accumulatedTokenSwapFees = balances[tokenIndex] - finalBalanceFeeToken
        else:
            accumulatedTokenSwapFees = 0

        return accumulatedTokenSwapFees

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

        invariant = calculateInvariant(amplificationParameter, balances)
        balances[tokenIndexOut] = balances[tokenIndexOut] - tokenAmountOut

        finalBalanceIn = getTokenBalanceGivenInvariantAndAllOtherBalances(
            amplificationParameter,
            balances,
            invariant,
            tokenIndexIn
        )

        balances[tokenIndexOut] = balances[tokenIndexOut]+ tokenAmountOut
        return finalBalanceIn - balances[tokenIndexIn] + 1/1e18


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

        invariant = calculateInvariant(amplificationParameter, balances)
        balances[tokenIndexIn] = balances[tokenIndexIn] + tokenAmountIn

        finalBalanceOut = getTokenBalanceGivenInvariantAndAllOtherBalances(amplificationParameter, balances, invariant, tokenIndexOut)
        balances[tokenIndexIn] = balances[tokenIndexIn] - tokenAmountIn

        return balances[tokenIndexOut] - finalBalanceOut  # TODO took out .sub(1) at the end of this statement


        # Flow of calculations:
        #  amountBPTOut -> newInvariant -> (amountInProportional, amountInAfterFee) ->
        #  amountInPercentageExcess -> amountIn

    @staticmethod
    def calcTokenInGivenExactBptOut(amplificationParameter: Decimal, balances: list[Decimal], tokenIndex: int, bptAmountOut: Decimal, bptTotalSupply: Decimal, swapFeePercentage: Decimal):
        # Token in so we round up overall

        #Get the current invariant
        currentInvariant = Decimal(calculateInvariant(amplificationParameter, balances))

        # Calculate new invariant
        newInvariant = divUp((bptTotalSupply + bptAmountOut), mulUp(bptTotalSupply, currentInvariant))

        # First calculate the sum of all token balances, which will be used
        # to calculate the current weight of each token
        sumBalances = Decimal(0)
        for i in range(len(balances)):
            sumBalances += i

        # get amountInAfterFee
        newBalanceTokenIndex = getTokenBalanceGivenInvariantAndAllOtherBalances(amplificationParameter, balances, newInvariant, tokenIndex)
        amountInAfterFee = newBalanceTokenIndex - balances[tokenIndex]

        # Get tokenBalancePercentageExcess
        currentWeight = divDown(balances[tokenIndex], sumBalances)
        tokenBalancePercentageExcess = complement(currentWeight)
        swapFeeExcess = mulUp(swapFeePercentage, tokenBalancePercentageExcess)

        return divUp(amountInAfterFee, complement(complement(swapFeeExcess)))

    @staticmethod
    def calcTokensOutGivenExactBptIn(balances: list[Decimal], bptAmountIn: Decimal, bptTotalSupply: Decimal):

        # /**********************************************************************************************
        # // exactBPTInForTokensOut                                                                    //
        # // (per token)                                                                               //
        # // aO = tokenAmountOut             /        bptIn         \                                  //
        # // b = tokenBalance      a0 = b * | ---------------------  |                                 //
        # // bptIn = bptAmountIn             \     bptTotalSupply    /                                 //
        # // bpt = bptTotalSupply                                                                      //
        # **********************************************************************************************/

        bptRatio = divDown(bptAmountIn, bptTotalSupply)
        amountsOut = []

        for i in range(len(balances)):
            amountsOut[i] = mulDown(balances[i], bptRatio)

        return amountsOut

        # Flow of calculations:
        #  amountBPTin -> newInvariant -> (amountOutProportional, amountOutBeforeFee) ->
        #  amountOutPercentageExcess -> amountOut

    @staticmethod
    def calcTokenOutGivenExactBptIn(amplificationParameter, balances: list[Decimal], tokenIndex: int, bptAmountIn: Decimal, bptTotalSupply: Decimal, swapFeePercentage: Decimal):
        # Get current invariant
        currentInvariant = calculateInvariant(amplificationParameter, balances)
        # calculate the new invariant
        newInvariant = bptTotalSupply - divUp(bptAmountIn, mulUp(bptTotalSupply, currentInvariant))

        # calculate the sum of all th etoken balances, which will be used to calculate
        # the current weight of each token
        sumBalances = Decimal(0)
        for i in range(len(balances)):
            sumBalances += i

        # get amountOutBeforeFee
        newBalanceTokenIndex = getTokenBalanceGivenInvariantAndAllOtherBalances(amplificationParameter, balances, newInvariant, tokenIndex)
        amountOutBeforeFee = balances[tokenIndex] - newBalanceTokenIndex

        # calculate tokenBalancePercentageExcess
        currentWeight = divDown(balances[tokenIndex], sumBalances)
        tokenbalancePercentageExcess = complement(currentWeight)

        swapFeeExcess = mulUp(swapFeePercentage, tokenbalancePercentageExcess)

        return mulDown(amountOutBeforeFee, complement(swapFeeExcess))


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

    @staticmethod
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

