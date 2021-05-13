from decimal import Decimal
from model.pools.BalancerPoolToken import BalancerPoolToken  

_MINIMUM_BPT = 1/1e6 

class BasePool:

    def __init__(self, vault: object, name: str, symbol: str, tokens: list, swap_fee_percentage: Decimal, owner_id: int):
        self.vault = vault
        self.name = name
        self.symbol = symbol
        self.tokens = tokens.sort()
        self.swap_fee_percentage = swap_fee_percentage
        self.owner_id = owner_id
        self.pool_id = None #vault.registerPool(specialization)

        self.paused = False
        self.balancer_pool_token = BalancerPoolToken(self.name, self.symbol)

    def get_vault(self) -> object:
        return self.vault
    
    def get_pool_id(self) -> int:
        return self.pool_id
        
    def get_total_tokens(self) -> int:
        return len(self.tokens)
    
    def get_swap_fee_percentage(self) -> Decimal:
        return self.swap_fee_percentage

    def set_swap_fee_percentage(self, swap_fee_percentage: Decimal):
        self.swap_fee_percentage = swap_fee_percentage
    
    def set_paused(self):
        self.paused = True

    def on_join_pool(self, sender_id: int, recipent_id: int, balances: list, protocol_swap_fee_percentage: Decimal):
        if(self.balancer_pool_token.total_supply() == 0):
           assert bpt_amount_out >= __MINIMUM_BPT
           self.balancer_pool_token.mint_pool_tokens(recipent_id, bpt_amount_out - _MINIMUM_BPT)
           amounts_in = {}
           return amounts_in
        else:
            bpt_amount_out, amounts_in, due_protocol_fee_amounts = _on_join_pool(pool_id, sender_id, recipent_id, balances, protocol_swap_fee_percentage)
            self.balancer_pool_token.mint_pool_tokens(recipent_id, bpt_amount_out)
            return amountsIn, due_protocol_amounts

    def on_exit_pool(self):
        ...
    
