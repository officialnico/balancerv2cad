from decimal import Decimal

class Vault:

    def __init__(self):
        ...

    def getInternalBalance(self, user_id: int, tokens: list):
        ...

    def manageUserBalance(self): #not sure if we should include
        ...

    def registerPool(self):
        ...

    def getPool(self):
        ...

    def registerTokens(self, poolId: int, tokens: list[Decimal], assetManagers: list[int]):
        ...

    def deregisterTokens(self, poolId: int, tokens: list[Decimal]):
        ...

    def getPoolTokenInfo(self, cash: Decimal, managed: Decimal, blockNumber: int, assetManager: int):
        ...

    def getPoolTokens(self, tokens: list, balances: list[Decimal], lastChangeBlock: int):
        ...

    def joinPool(self, poolId: int, sender_id: int, recipent_id: int):
        ...

    def exitPool(poolId: int, sender: int, recipient: int):
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
