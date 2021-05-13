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
		balance_out = Decimal(100)
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

	def test_calc_token_in_given_exact_bpt_out(weightedmath_test):
		balance = Decimal(1)
		normalized_weight = Decimal(10)
		bpt_amount_out = Decimal(10)
		bpt_total_supply = Decimal(10)
		swap_fee = Decimal(10)
		result = WeightedMath.calc_token_in_given_exact_bpt_out(balance, normalized_weight, bpt_amount_out, bpt_total_supply, swap_fee)
		assert isinstance(result, Decimal)

	def test_calc_bpt_in_given_exact_tokens_out(weightedmath_test):
		balances = [Decimal(10), Decimal(12), Decimal(14)]
		normalized_weights = [Decimal(10), Decimal(12), Decimal(14)]
		bpt_amount_out = [Decimal(10), Decimal(12), Decimal(14)]
		bpt_total_supply = Decimal(1)
		swap_fee = Decimal(1)
		result = WeightedMath.calc_bpt_in_given_exact_tokens_out(balances, normalized_weights, bpt_amount_out, bpt_total_supply, swap_fee)
		assert isinstance(result, Decimal)

	def test_calc_token_out_given_exact_bpt_in(weightedmath_test):
		balance = Decimal(10)
		normalized_weight = Decimal(10)
		bpt_amount_in = Decimal(2)
		bpt_total_supply = Decimal(10)
		swap_fee = Decimal(0)
		result = WeightedMath.calc_token_out_given_exact_bpt_in(balance, normalized_weight, bpt_amount_in, bpt_total_supply, swap_fee)
		assert isinstance(result, Decimal)

	def test_calc_tokens_out_given_exact_bpt_in(weightedmath_test):
		balance = Decimal(10)
		normalized_weight = Decimal(1)
		bpt_amount_in = Decimal(2)
		bpt_total_supply = Decimal(1)
		swap_fee = Decimal(1)
		result = WeightedMath.calc_token_out_given_exact_bpt_in(balance, normalized_weight, bpt_amount_in, bpt_total_supply, swap_fee )
		assert isinstance(result, Decimal)

	def test_calc_due_token_protocol_swap_fee_amount(weightedmath_test):
		balance = Decimal(10)
		normalized_weight = Decimal(10)
		previous_invariant = Decimal(20)
		current_invariant = Decimal(4)
		protocol_swap_fee_percentage = Decimal(1)
		result = WeightedMath.calc_due_token_protocol_swap_fee_amount(balance, normalized_weight, previous_invariant, current_invariant, protocol_swap_fee_percentage)
		assert isinstance(result, Decimal)
		# TODO also looks different form the .sol file
