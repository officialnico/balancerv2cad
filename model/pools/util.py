from decimal import *


def mulUp(a: Decimal, b: Decimal):
    getcontext().prec = 18
    getcontext().rounding = ROUND_UP
    return a*b


def divUp(a: Decimal, b: Decimal):
    getcontext().prec = 18
    getcontext().rounding = ROUND_UP
    return a/b


def mulDown(a: Decimal, b: Decimal):
    getcontext().prec = 18
    getcontext().rounding = ROUND_DOWN
    return a*b


def divDown(a: Decimal, b: Decimal):
    getcontext().prec = 18
    getcontext().rounding = ROUND_DOWN
    return a/b


def complement(a: int) -> int:
    return 1 - a if a < 1 else 0


def powUp(a,b):
    getcontext().prec = 18
    getcontext().rounding = ROUND_UP
    return a**b


def powDown(a,b):
    getcontext().prec = 18
    getcontext().rounding = ROUND_DOWN
    return a**b
