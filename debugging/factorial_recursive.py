#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <non-negative integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    print(factorial(num))
except ValueError as e:
    print("Error:", e)

