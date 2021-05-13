from decimal import Decimal

class BasePool:

    def __init__(self, vault: object, name: str, symbol: str, tokens: list, swap_fee_percentage: Decimal, owner_id: int):
        self.vault = vault
        self.name = name
        self.symbol = symbol
        self.tokens = tokens.sort()
        self.swap_fee_percentage = swap_fee_percentage
        self.owner_id = owner_id
        self.poolId = None #vault.registerPool(specialization)
        self.paused = False

    def get_vault(self) -> object:
        return self.vault
    
    def get_pool_id(self) -> int:
        return self.poolId
        
    def get_total_tokens(self) -> int:
        return len(self.tokens)
    
    def get_swap_fee_percentage(self) -> Decimal:
        return self.swapFeePercentage

    def set_swap_fee_percentage(self, swap_fee_percentage: Decimal):
        self.swap_fee_percentage = swap_fee_percentage
    
    def set_paused(self):
        self.paused = True

    def on_join_pool(self):
        #if totalSupply() = 0
        ...
    
    def on_exit_pool(self):
        ...
    
