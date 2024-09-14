#!/usr/bin/python3
"""
Module for minimum number of operations to reach n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in exactly
    n 'H' characters in the file.

    Operations:
    - Copy All: copy all the characters in the file
    - Paste: paste the copied characters

    Args:
    n (int): Target number of 'H' characters.

    Returns:
    int: Minimum number of operations, or 0 if it's impossible to achieve n characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # We keep dividing n by its factors until n becomes 1
    while n > 1:
        # If n is divisible by the factor, perform Paste operation
        while n % factor == 0:
            operations += factor  # Adding the factor as the number of operations
            n //= factor
        factor += 1

    return operations

