from decimal import Decimal
from model.pools.stable.StableMath import StableMath


class StablePool(StableMath):

    def __init__(self, vault: object, name: str, symbol: str, tokens: list, amplification_parameter: Decimal, swap_fee_percentage: Decimal, owner_id: int):
        self.vault = vault
        self.name = name
        self.symbol = symbol
        self.tokens = sorted(tokens)
        self.amplification_parameter = amplification_parameter
        self.swap_fee_percentage = swap_fee_percentage
        self.owner_id = owner_id
        self.pool_id = None #vault.registerPool(specialization)
        self.paused = False
    
    def get_amplification_parameter(self):
        return self.amplification_parameter
    def get_vault(self):
        return self.vault
    def get_pool_id(self):
        return self.pool_id
    def get_owner_id(self):
        return self.owner_id
    def get_total_tokens(self):
        return len(self.tokens)
    def get_swap_fee_percentage(self):
        return self.swap_fee_percentage
    def set_paused(self):
        self.paused = True
    def on_join_pool(self):
        NotImplementedError
    def on_exit_pool(self):
        NotImplementedError
    def joinExactTokensInForBPTOut(self ):
        NotImplementedError
    