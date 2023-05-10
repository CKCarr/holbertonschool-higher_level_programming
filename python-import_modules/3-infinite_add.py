#!/usr/bin/python3
import sys
from decimal import Decimal
if __name__ == "__main__":
    args = sys.argv[1:]
    result = sum(Decimal(arg) for arg in args)
    print(result)
