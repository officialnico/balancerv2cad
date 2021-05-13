from decimal import *
from enforce_typing import enforce_types
@enforce_types
def mulUp(a: Decimal, b: Decimal)-> Decimal:
    getcontext().prec = 18
    getcontext().rounding = ROUND_UP
    return a*b

@enforce_types
def divUp(a: Decimal, b: Decimal)-> Decimal:
    if a * b == 0:
        return 0
    else:
        getcontext().prec = 18
        getcontext().rounding = ROUND_UP
        return a/b

@enforce_types
def mulDown(a: Decimal, b: Decimal)-> Decimal:
    getcontext().prec = 18
    getcontext().rounding = ROUND_DOWN
    return a * b

@enforce_types
def divDown(a: Decimal, b: Decimal)-> Decimal:
    getcontext().prec = 18
    getcontext().rounding = ROUND_DOWN
    return a/b

@enforce_types
def complement(a: Decimal) -> Decimal:
    
    return Decimal(1 - a) if a < 1 else Decimal(0)

@enforce_types
def powUp(a: Decimal,b:Decimal) -> Decimal:
    getcontext().prec = 18
    getcontext().rounding = ROUND_UP
    return a**b

@enforce_types
def powDown(a: Decimal,b: Decimal)-> Decimal:
    getcontext().prec = 18
    getcontext().rounding = ROUND_DOWN
    return a**b
