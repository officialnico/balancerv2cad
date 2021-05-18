from decimal import *
from typing import List
from model.pools.stable.StableMath import StableMath

getcontext().prec = 18
class StablePool(StableMath):

    def __init__(self, vault: object, name: str, symbol: str, tokens: list, amplification_parameter: Decimal, swap_fee_percentage: Decimal, owner_id: int):
        self.vault = vault
        self.name = name
        self.symbol = symbol
        self.tokens = sorted(tokens)
        self._amplification_parameter = amplification_parameter
        self.swap_fee_percentage = swap_fee_percentage
        self.owner_id = owner_id
        self.pool_id = None #vault.registerPool(specialization)
        self.paused = False
    
    def _invariant_after_join(self, balances: List[Decimal]):
        ...

    # Base Pool Handlers
    def on_swap_given_in(self, balances: List[Decimal], index_in: int, index_out: int):
        amp = self.get_amplification_parameter()
        amount_out = StablePool.calcOutGivenIn(amp,balances, index_in, index_out)
        return amount_out

    def on_swap_given_out(self, balances: List[Decimal], index_in: int, index_out: int):
        amp = self.get_amplification_parameter()
        amount_out = StablePool.calcOutGivenOut(amp,balances,index_in, index_out)
        return amount_out

    def get_amplification_parameter(self):
        return self._amplification_parameter
    def get_vault(self):
        return self.vault
    def get_pool_id(self):
        return self.pool_id
    def get_owner_id(self):
        return self.owner_id
    def _get_total_tokens(self):
        return len(self.tokens)
    def get_swap_fee_percentage(self):
        return self.swap_fee_percentage
    def set_paused(self):
        self.paused = True
    def on_join_pool(self, balances: List[Decimal], protocl_swap_fee_percentage: Decimal):
        due_protocol_fee_amounts = self._get_due_protocol_fees_amounts(balances,  )


    def on_exit_pool(self):
        NotImplementedError
    def joinExactTokensInForBPTOut(self ):
        NotImplementedError
    

    def _get_due_protocol_fees_amounts(self, balances: List[Decimal], previous_invariant: Decimal, protocol_swap_fee_percentage: Decimal)-> List[Decimal]: 
        due_protocol_amounts = [0]*self._get_total_tokens()
        if protocol_swap_fee_percentage == Decimal(0):
            return due_protocol_amounts

        chosen_token_index = 0
        max_balance = balances[0]
        for i in range(1, self._get_total_tokens()):
            current_balance = balances[i]
            if current_balance > max_balance:
                chosen_token_index = i
                max_balance = current_balance
        due_protocol_amounts[chosen_token_index] = StablePool.calcDueTokenProtocolSwapFeeAmount(self._amplification_parameter, balances,previous_invariant, chosen_token_index, protocol_swap_fee_percentage)
        return due_protocol_amounts