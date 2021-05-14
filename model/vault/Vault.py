from decimal import Decimal
from typing import List


class Vault:

    def __init__(self):
        self.pool_balances = []

    def get_internal_balance(self, user_id: int, tokens: list):
        ...

    def manage_user_balance(self): #not sure if we should include
        ...

    def register_pool(self): #return pool id
        ...

    def get_pool(self):
        ...

    def register_tokens(self, poolId: int, tokens: List[Decimal], assetManagers: List[int]):
        ...

    def deregister_tokens(self, poolId: int, tokens: List[Decimal]):
        ...

    def get_pool_token_info(self, cash: Decimal, managed: Decimal, blockNumber: int, assetManager: int):
        ...

    def get_pool_tokens(self, tokens: list, balances: List[Decimal], lastChangeBlock: int):
        ...

    def join_pool(self, poolId: int, sender_id: int, recipent_id: int):
        ...

    def exit_pool(poolId: int, sender: int, recipient: int):
        ...

    

#     def swap(
#     SingleSwap request, 
#     FundManagement funds, 
#     uint256 limit, 
#     uint256 deadline) 
# returns (uint256 assetDelta)

# batchSwap(
#     SwapKind kind,
#     BatchSwapStep[] swaps, 
#     IAsset[] assets, 
#     FundManagement funds, 
#     int256[] limits, 
#     uint256 deadline) 
# returns (int256[] assetDeltas)

# queryBatchSwap(
#     SwapKind kind, 
#     BatchSwapStep[] swaps, 
#     IAsset[] assets, 
#     FundManagement funds) 
# returns (int256[] assetDeltas)

# flashLoan(
#     IFlashLoanRecipient recipient, 
#     IERC20[] tokens, 
#     uint256[] amounts, 
#     bytes userData)
    
# managePoolBalance(
#     PoolBalanceOp[] ops)
