from decimal import Decimal

class BalancerPoolToken:

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.balances = {}

    def name(self):
        return self.name

    def symbol(self):
        return self.symbol

    def total_supply(self):
        return sum(self.balances)

    def mint_pool_tokens(self, user_id: int, amount: Decimal):
        if(self.balances[user_id] is None): self.balances[user_id] = 0
        self.balances[user_id] =  self.balances[user_id] + amount

    def burn_pool_tokens(self, user_id: int, amount: Decimal):
        if(self.balances[user_id] is None): self.balances[user_id] = 0
        ret = self.balances[user_id] - amount
        if(ret<0): ret = 0
        self.balances[user_id] = ret

    def transfer(self, sender_id: int, recipent_id: int, amount):
        if(self.balances[sender_id] is None): self.balances[sender_id] = 0
        if(self.balances[recipent_id] is None): self.balances[recipent_id] = 0
        if(amount>self.balances[sender_id]): amount = self.balances[sender_id] #TODO maybe replace with assert
        self.balances[sender_id] -= amount
        self.balances[recipent_id] += amount

        
