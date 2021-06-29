from decimal import *
from typing import List
from balancerv2cad.StableMath import StableMath
from balancerv2cad.WeightedPool import WeightedPool
from balancerv2cad.BalancerConstants import *


class StablePool(StableMath):

    def __init__(self, initial_pool_supply: Decimal = INIT_POOL_SUPPLY):
        self._wp = WeightedPool(INIT_POOL_SUPPLY)

    def swap(self, token_in: str, token_out: str, amount: Decimal, given_in: bool = True):
        return self._wp.swap(token_in, token_out, amount, given_in)

    def join_pool(self, balances: dict):
        if(len(balances) != 2 or len(self._wp._balances)==2 and self._wp._balances.keys()!=balances.keys()):
            raise Exception("50/50 2-token pool only")
        weights = {}
        for key in balances:
            weights.update({key:0.5})
        self._wp.join_pool(balances,weights)

    def get_amplification_parameter(self):
        return self._wp.AMPLIFICATION_PARAMETER

    def _get_total_tokens(self):
        return len(self._wp._balances)

    def exit_pool(self, balances: dict):
        self._wp.exit_pool(balances)

    def set_swap_fee(self, amount: Decimal):
        self._wp.set_swap_fee(amount)

    def _mint_pool_share(self, amount: Decimal):
        self._wp._pool_token_supply += amount

    def _burn_pool_share(self, amount: Decimal):
        self._wp._pool_token_supply -= amount

    def get_balances(self):
        return self._wp._balances

    def get_factory_fees(self):
        return self._wp.factory_fees