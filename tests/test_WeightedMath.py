from decimal import Decimal
from model.pools.weighted.WeightedMath import WeightedMath


class TestWeightedMath:

	def test_calculate_invariant(weightedmath_test):
		normalized_weight = [Decimal(0.3), Decimal(0.2), Decimal(0.5)]
		balances = [Decimal(10), Decimal(12), Decimal(14)]
		result = WeightedMath.calculate_invariant(normalized_weight, balances)
		assert isinstance(result, Decimal)


	def test_calc_out_given_in(weightedmath_test):
		balance_in = Decimal(100)
		weight_in = Decimal(0.00769)
		balance_out =  Decimal(100)
		weight_out = Decimal(1)
		amount_out = Decimal(15)
		result = WeightedMath.calc_out_given_in(balance_in, weight_in, balance_out, weight_out, amount_out)
		assert isinstance(result, Decimal)

	def test_calc_bpt_out_given_exact_tokens_in(weightedmath_test):
		balances = [Decimal(10), Decimal(12), Decimal(14)]
		normalized_weights = [Decimal(10), Decimal(12), Decimal(14)]
		amounts_in = [Decimal(10), Decimal(12), Decimal(14)]
		bpt_total_supply = Decimal(1)
		swap_fee = Decimal(1)
		result = WeightedMath.calc_bpt_out_given_exact_tokens_in(balances, normalized_weights, amounts_in, bpt_total_supply, swap_fee)
		assert isinstance(result, Decimal)


	def test_calcTokenInGivenExactBptOut(weightedmath_test):
		balance = Decimal(1)
		normalizedWeight = Decimal(10)
		bptAmountOut = Decimal(10)
		bptTotalSupply = Decimal(10)
		swap_fee = Decimal(10)
		result = WeightedMath.calcTokenInGivenExactBptOut(balance, normalizedWeight, bptAmountOut, bptTotalSupply, swap_fee)
		assert isinstance(result, Decimal)

	def test_calcBptInGivenExactTokensOut(weightedmath_test):
		balances = [Decimal(10), Decimal(12), Decimal(14)]
		normalized_weights = [Decimal(10), Decimal(12), Decimal(14)]
		bptAmountOut = [Decimal(10), Decimal(12), Decimal(14)]
		bptTotalSupply = Decimal(1)
		swapFee = Decimal(1)
		result = WeightedMath.calcBptInGivenExactTokensOut(balances, normalized_weights, bptAmountOut, bptTotalSupply, swapFee)
		assert isinstance(result, Decimal)


