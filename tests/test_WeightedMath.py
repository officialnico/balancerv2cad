from decimal import Decimal
from model.pools.weighted.WeightedMath import WeightedMath


class TestWeightedMath:

	def test_calculate_invariant(weightedmath_test):
		normalized_weight = [Decimal(0.3), Decimal(0.2), Decimal(0.5)]
		balances = [Decimal(10), Decimal(12), Decimal(14)]
		result = WeightedMath.calculate_invariant(normalized_weight, balances)
		assert isinstance(result, Decimal)


