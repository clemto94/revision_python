"""
Given an integer max_val and another integer a, return the biggest integer b such that a^b #
max_val .
As a reminder: a^b = ab = a * a * a * ... (a multiplied b times).
For example, if max_val is 33, and a is 2, you must return 5, as 2^5 = 32.
"""

from json import dumps, loads
import sys
from typing import List

def find_power(max_val: int, a: int) -> int:
    """
    Trouve la plus grande puissance b telle que a^b ≤ max_val.

    Args:
        max_val (int): La valeur maximale autorisée
        a (int): La base qui sera élevée à une puissance spécifique

    Returns:
        int: La plus grande puissance qui respecte l'équation
    """
    b = 0
    p = 1
    while p <= max_val:
        b += 1
        p *= a
    return b - 1

def try_solution(output: int):
    """
    Teste une solution

    Args:
        output (int): La plus grande puissance qui respecte l'équation
    """
    json = output
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = find_power(
        loads(input()),
        loads(input())
    )
    try_solution(res)

if __name__ == "__main__":
    main()