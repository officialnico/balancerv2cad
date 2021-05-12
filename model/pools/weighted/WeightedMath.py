from decimal import Decimal
from model.pools.util import *
from typing import List

MIN_WEIGHT = 0.01
_MAX_WEIGHTED_TOKENS = 100
_MAX_IN_RATIO = 0.3
_MAX_OUT_RATIO = 0.3
_MAX_INVARIANT_RATIO = 3
_MIN_INVARIANT_RATIO = 0.7

class WeightedMath:

    @staticmethod
    def calculate_invariant(normalized_weights: List[Decimal], balances: List[Decimal]):

        # /**********************************************************************************************
        # // invariant               _____                                                             //
        # // wi = weight index i      | |      wi                                                      //
        # // bi = balance index i     | |  bi ^   = i                                                  //
        # // i = invariant                                                                             //
        # **********************************************************************************************/

        invariant = 1
        for i in range(len(normalized_weights)):
            invariant = mulDown(invariant, (powDown(balances[i], normalized_weights[i])))
        return invariant

    @staticmethod
    def calc_out_given_in(balance_in: Decimal, weight_in: Decimal,
                          balance_out: Decimal,
                          weight_out: Decimal,
                          amount_in: Decimal) -> Decimal:

        # /**********************************************************************************************
        # // outGivenIn                                                                                //
        # // aO = amountOut                                                                            //
        # // bO = balanceOut                                                                           //
        # // bI = balanceIn              /      /            bI             \    (wI / wO) \           //
        # // aI = amountIn    aO = bO * |  1 - | --------------------------  | ^            |          //
        # // wI = weightIn               \      \       ( bI + aI )         /              /           //
        # // wO = weightOut                                                                            //
        # **********************************************************************************************/

        denominator = balance_in + amount_in
        base = divUp(balance_in, denominator) #balanceIn.divUp(denominator);
        exponent = divDown(weight_in, weight_out) #weightIn.divDown(weightOut);
        power = powUp(base,exponent) #base.powUp(exponent);

        return mulDown(balance_out, complement(power)) #balanceOut.mulDown(power.complement());

    @staticmethod
    def calc_in_given_out(balance_in: Decimal,
                          weight_in: Decimal,
                          balance_out: Decimal,
                          weight_out: Decimal,
                          amount_out: Decimal):

        # /**********************************************************************************************
        # // inGivenOut                                                                                //
        # // aO = amount_out                                                                            //
        # // bO = balance_out                                                                           //
        # // bI = balance_in              /  /            bO             \    (wO / wI)      \          //
        # // aI = amount_in    aI = bI * |  | --------------------------  | ^            - 1  |         //
        # // wI = weight_in               \  \       ( bO - aO )         /                   /          //
        # // wO = weight_out                                                                            //
        # **********************************************************************************************/

        base = divUp(balance_out, (balance_out - amount_out))
        exponent = divUp(weight_out, weight_in)
        power = powUp(base, exponent)
        ratio = power - 1
        return mulUp(balance_in, ratio)

    @staticmethod
    def calc_bpt_out_given_exact_tokens_in(balances: List[Decimal], normalized_weights: List[Decimal], amountsIn: List[Decimal],
        bptTotalSupply: Decimal,
        swap_fee: Decimal):

        balanceRatiosWithFee = [None]*len(amountsIn)
        invariantRatioWithFees = 0
        for i in range(len(balances)):
            # balanceRatiosWithFee[i] = balances[i].add(amountsIn[i]).divDown(balances[i]);
            # invariantRatioWithFees = invariantRatioWithFees.add(balanceRatiosWithFee[i].mulDown(normalized_weights[i]));
            balanceRatiosWithFee[i] = divDown((balances[i] + amountsIn[i]),balances[i])
            invariantRatioWithFees = mulDown((invariantRatioWithFees + balanceRatiosWithFee[i]),normalized_weights[i]) #.add(balanceRatiosWithFee[i].mulDown(normalized_weights[i]));

        invariantRatio = 1
        for i in range(len(balances)):
            amountInWithoutFee = None

            if(balanceRatiosWithFee[i] > invariantRatioWithFees):
                nonTaxableAmount = mulDown(balances[i],(invariantRatio-1))
                taxableAmount = amountsIn[i] - nonTaxableAmount
                amountInWithoutFee = nonTaxableAmount + (mulDown(taxableAmount, 1 - swap_fee))
            else:
                amountInWithoutFee = amountsIn[i]

            balanceRatio = divDown((balances[i]+amountInWithoutFee),balances[i])
            invariantRatio = mulDown(invariantRatio,(powDown(balanceRatio,normalized_weights[i])))

        if(invariantRatio>=1):
            return mulDown(bptTotalSupply,(invariantRatio-1))
        else:
            return 0

    @staticmethod
    def calcTokenInGivenExactBptOut(
        balance: Decimal,
        normalizedWeight: Decimal,
        bptAmountOut: Decimal,
        bptTotalSupply: Decimal,
        swap_fee: Decimal
    ) -> Decimal:

        # /******************************************************************************************
        # // tokenInForExactBPTOut                                                                 //
        # // a = amountIn                                                                          //
        # // b = balance                      /  /    totalBPT + bptOut      \    (1 / w)       \  //
        # // bptOut = bptAmountOut   a = b * |  | --------------------------  | ^          - 1  |  //
        # // bpt = totalBPT                   \  \       totalBPT            /                  /  //
        # // w = weight                                                                            //
        # ******************************************************************************************/

        invariantRatio = divUp((bptTotalSupply + bptAmountOut),bptTotalSupply)
        balanceRatio = powUp(invariantRatio,(divUp(1,normalizedWeight)))
        amountInWithoutFee = mulUp(balance, (balanceRatio-1))
        taxablePercentage = complement(normalizedWeight)
        taxableAmount = mulUp(amountInWithoutFee, taxablePercentage)
        nonTaxableAmount = amountInWithoutFee - taxableAmount
        return nonTaxableAmount + (divUp(taxableAmount, complement(swap_fee)))

    @staticmethod
    def calcBptInGivenExactTokensOut(
        balances: list[Decimal],
        normalizedWeights: list[Decimal],
        bptAmountOut: list[Decimal],
        bptTotalSupply: Decimal,
        swap_fee: Decimal
    ) -> Decimal:

        balanceRatiosWithoutFee = [None]*len(amountsOut)
        invariantRatioWithoutFees = 0
        for i in range(len(balances)):
            balanceRatiosWithoutFee[i] = divUp((balances[i]-amountsOut[i]),balances[i])
            invariantRatioWithoutFees = invariantRatioWithoutFees + (mulUp(balanceRatiosWithoutFee[i],normalizedWeights[i]))

        invariantRatio = 1
        for i in range(len(balanes)):
            amountOutWithFee = None
            if(invariantRatioWithoutFees>balanceRatiosWithoutFee[i]):
                nonTaxableAmount = mulDown(balances[i],(complement(invariantRatioWithoutFees)))
                taxableAmount = amountsOut[i] - nonTaxableAmount
                amountOutWithFee = nonTaxableAmount+(divUp(taxableAmount, complement(swap_fee)))
            else:
                amountOutWithFee = amountsOut[i]
            balanceRatio = divUp((balances[i]-amountOutWithFee),balances[i])
            invariantRatio = mulDown(invariantRatio,(powDown(balanceRatio,normalizedWeights[i])))
        return mulUp(bptTotalSupply,complement(invariantRatio))

    @staticmethod
    def calcTokenOutGivenExactBptIn(
        balance: Decimal,
        normalizedWeight: Decimal,
        bptAmountIn: Decimal,
        bptTotalSupply: Decimal,
        swapFee: Decimal
    ) -> Decimal:

        # /*****************************************************************************************
        # // exactBPTInForTokenOut                                                                //
        # // a = amountOut                                                                        //
        # // b = balance                     /      /    totalBPT - bptIn       \    (1 / w)  \   //
        # // bptIn = bptAmountIn    a = b * |  1 - | --------------------------  | ^           |  //
        # // bpt = totalBPT                  \      \       totalBPT            /             /   //
        # // w = weight                                                                           //
        # *****************************************************************************************/

        invariantRatio = divUp((bptTotalSupply - bptAmountIn), bptTotalSupply)
        balanceRatio = powUp(invariantRatio, (divDown(1,normalizedWeight)))
        amountOutWithoutFee = mulDown(balance, complement(balanceRatio))
        taxablePercentage = complement(normalizedWeight)
        taxableAmount = mulUp(amountOutWithoutFee, taxablePercentage)
        nonTaxableAmount = amountOutWithoutFee - taxableAmount

        return nonTaxableAmount + mulDown(taxableAmount,complement(swapFee))

    @staticmethod
    def calcTokensOutGivenExactBptIn(
        balances: list[Decimal],
        bptAmountIn: Decimal,
        totalBPT: Decimal
    ) -> Decimal:

        # /**********************************************************************************************
        # // exactBPTInForTokensOut                                                                    //
        # // (per token)                                                                               //
        # // aO = amountOut                  /        bptIn         \                                  //
        # // b = balance           a0 = b * | ---------------------  |                                 //
        # // bptIn = bptAmountIn             \       totalBPT       /                                  //
        # // bpt = totalBPT                                                                            //
        # **********************************************************************************************/

        bptRatio = divDown(bptAmountIn,totalBPT)
        amountsOut = [None]*len(balances)
        for i in range(balances):
            amountsOut[i] = mulDown(balances[i],bptRatio)
        return amountsOut

    @staticmethod
    def calcDueTokenProtocolSwapFeeAmount(
        balance: Decimal,
        normalizedWeight: Decimal,
        previousInvariant: Decimal,
        currentInvariant: Decimal,
        protocolSwapFeePercentage: Decimal) -> Decimal:

        # /*********************************************************************************
        # /*  protocolSwapFeePercentage * balanceToken * ( 1 - (previousInvariant / currentInvariant) ^ (1 / weightToken))
        # *********************************************************************************/

        if(currentInvariant <= previousInvariant):
            return 0

        base = divUp(previousInvariant, currentInvariant)
        exponent = divDown(1,normalizedWeight)
        base = max(base, 0.7)
        power = powUp9(base, exponent)
        tokenAccruedFees = mulDown(balance, (complement(power)))
        return mulDown(tokenAccruedFees, protocolSwapFeePercentage);
