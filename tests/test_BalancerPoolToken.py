from typing import List
from model.pools.BalancerPoolToken import BalancerPoolToken
from decimal import Decimal
import unittest

class TestBalancerPoolTokenMath(unittest.TestCase):

	def test_name(balancerpooltoken_test):
		bpt = BalancerPoolToken("Ethereum", "ETH")
		assert bpt.name == "Ethereum"

	def test_symbol(balancerpooltoken_test):
		bpt = BalancerPoolToken("Ethereum", "ETH")
		assert bpt.symbol == "ETH"

	def test_total_supply(balancerpooltoken_test):
		pass

	def test_mint_pool_tokens(balancerpooltoken_test):
		bpt = BalancerPoolToken("Ethereum", "ETH")
		old_balance = balances[0]
		bpt.mint_pool_tokens(0, Decimal(10))
		new_balances = balances[0]
		assert old_balances + Decimal(10) == new_balances
		# TODO: logic

	def test_burn_pool_tokens(self):

