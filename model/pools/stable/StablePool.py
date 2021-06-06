from decimal import *
from typing import List
from model.pools.stable.StableMath import StableMath
from model.pools.BalancerConstants import *


class StablePool(StableMath):

    def __init__(self, initial_pool_supply: Decimal = INIT_POOL_SUPPLY):
        self._swap_fee = MIN_FEE
        self._pool_token_supply = initial_pool_supply
        self.factory_fees = Decimal('0')
        self._balances = {}
        self._amplification_parameter = AMPLIFICATION_PARAMETER

    def swap(self, token_in: str, token_out: str, amount: Decimal, given_in: bool = True):
        if(isinstance(amount,int) or isinstance(amount,float)):
            amount = Decimal(amount)
        elif(not isinstance(amount, Decimal)):
            raise Exception("INCORRECT_TYPE")
        factory_fee = amount*self._swap_fee
        swap_amount = amount - factory_fee
        self.factory_fees += factory_fee
        balances = [self._balances[token_in], self._balances[token_out]]
        
        if(given_in): amount_out = StableMath.calc_out_given_in(AMPLIFICATION_PARAMETER, balances, 0, 1, swap_amount)
        else: amount_out = StableMath.calc_in_given_out(AMPLIFICATION_PARAMETER, balances, 0, 1, swap_amount)
        
        self._balances[token_out] -= amount_out
        self._balances[token_in] += swap_amount
        return amount_out
    
    
    def join_pool(self, balances: dict):
        
        for key in balances:
            if key in self._balances:
                self._balances[key] += balances[key]
            else:
                self._balances.update({key:balances[key]})
    
    def get_amplification_parameter(self):
        return self._amplification_parameter

    def _get_total_tokens(self):
        return len(self._balancesa)

    def exit_pool(self, balances: dict):
        bals = self._balances - balances
        for key in bals:
            if(bals[key]<0): bals[key] = 0
        self._balances = bals
    def set_swap_fee(self, amount: Decimal):
        self._swap_fee = amount

    def _mint_pool_share(self, amount: Decimal):
        self._pool_token_supply += amount
        
    def _burn_pool_share(self, amount: Decimal):
        self._pool_token_supply -= amount
        