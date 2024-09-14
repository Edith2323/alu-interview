#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to result in exactly
n 'H' characters in a text file.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in exactly
    n 'H' characters in the file.

    Operations allowed:
    - Copy All: copy all the characters in the file.
    - Paste: paste the copied characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations to reach exactly n characters, or
        0 if it's impossible to achieve n characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Divide n by its factors until n becomes 1
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

