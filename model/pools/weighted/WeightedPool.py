from decimal import Decimal
from model.pools.weighted.WeightedMath import WeightedMath

BONE = Decimal('1')
MIN_FEE = Decimal('0.000001')
MAX_FEE = Decimal('0.1')
INIT_POOL_SUPPLY = BONE * Decimal('100')
MIN_BOUND_TOKENS = 2
MAX_BOUND_TOKENS = 8
AMPLIFICATION_PARAMETER = Decimal('200')

class WeightedPool(WeightedMath):

    def __init__(self, initial_pool_supply: Decimal = INIT_POOL_SUPPLY):
        self._swap_fee = MIN_FEE
        self.total_weight = Decimal('0')
        self._pool_token_supply = initial_pool_supply
        self.factory_fees = Decimal('0')
        self._balances = {}
        self._weights = {}


    def weighted_swap(self, token_in: str, token_out: str, amount: Decimal, given_in: bool = True):
        assert len(self._weights) == len(self._balances)
        if(isinstance(amount,int) or isinstance(amount,float)):
            amount = Decimal(amount)
        elif(not isinstance(amount, Decimal)):
            raise Exception("INCORRECT_TYPE")
        factory_fee = amount*self._swap_fee
        swap_amount = amount - factory_fee
        self.factory_fees += factory_fee
        balances = [self._balances[token_in], self._balances[token_out]]
        weights = [self._weights[token_in], self._weights[token_out]]
        
        if(given_in): amount_out = WeightedMath.calc_out_given_in(balances[0], weights[0], balances[1], weights[1], amount)
        else: WeightedMath.calc_in_given_out(balances[0], weights[0], balances[1], weights[1], amount)
            
        self._balances[token_out] -= amount_out
        self._balances[token_in] += swap_amount
        return amount_out
    
    def join_pool(self, balances: dict, weights: dict):
        for key in weights:
            if(not isinstance(weights[key],Decimal)):
               weights[key] = Decimal(weights[key])
            if(not isinstance(balances[key],Decimal)):
               balances[key] = Decimal(balances[key])
            
        for key in balances:
            if key in self._balances:
                self._balances[key] += balances[key]
            else:
                self._balances.update({key:balances[key]})
        self._weights = weights

        if(len(self._balances)>8):
            raise Exception("over 8 tokens")
    
    def exit_pool(self, balances: dict):
        bals = self._balances - balances
        for key in bals:
            if(bals[key]<0): bals[key] = 0
        self._balances = bals
         
    def _mint_pool_share(self, amount: Decimal):
        self._pool_token_supply += 1
        
    def _burn_pool_share(self, amount: Decimal):
        self._pool_token_supply -= 1
        
    def set_swap_fee(self, amount: Decimal):
        self._swap_fee = amount
        

    
