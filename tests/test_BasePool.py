from typing import List
from model.pools.BasePool import BasePool
from decimal import Decimal
import unittest


class TestBasePool(unittest.TestCase):

	def test_get_vault(basepool_test):
		result = basepool_test.get_vault()
		assert isinstance(result, object)

	def test_get_pool_id(basepool_test):
		assert basepool_test.get_pool_id() == 0

	def test_get_total_tokens(basepool_test):
		assert basepool_test.get_total_tokens() == 2

	def test_get_swap_fee_percentage(basepool_test):
		fee = basepool_test.get_swap_fee_percentage()
		assert fee == Decimal(0.23)

	def test_set_swap_fee_percentage(selfbasepool_test):
		fee = basepool_test.set_swap_fee_percentage(Decimal(0.24))
		assert fee == Decimal(0.24)





