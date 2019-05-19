import math
from decimal import Decimal

## FORMULA --> n = (-1 + sqrt(1 + 8*sqrt(x))) / 2

def find_nb(m):
    base = 8 * (Decimal(m) ** Decimal(0.5))

    if base % 1 == 0:
        n = math.sqrt(1+base) - 1
        n = n/2
        return int(n) if n % 1 == 0 else -1
    else:
        return -1
