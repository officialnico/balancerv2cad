from typing import List
from model.pools.BasePool import BasePool
from decimal import Decimal
import unittest


class TestBasePool(unittest.TestCase):

	def test_get_vault(basepool_test):
		b = BasePool()
		b.vault = BasePool.vault
		result = b.get_vault()
		assert isinstance(result, object)

	def test_get_pool_id(basepool_test):


	def test_get_total_tokens(basepool_test):
		a, b = BasePool, BasePool
		a.tokens = []
		b.tokens = ['eth', 'btc']
		assert a.get_total_tokens() == 0
		assert b.get_total_tokens() == 2

	def test_get_swap_fee_percentage(basepool_test):
		b = BasePool
		b.swap_fee_percentage = 20
		assert b.get_swap_fee_percentage() == 20

	def test_set_swap_fee_percentage(selfbasepool_test):
		b = BasePool
		b.





