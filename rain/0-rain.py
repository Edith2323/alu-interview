#!/usr/bin/python3
"""
This module contains the 'rain' function which calculates
the amount of water retained after rainfall, given a list
of wall heights.
"""


def rain(walls):
    """
    This function calculates how many square units of water
    will be retained after it rains, given a list of walls
    with non-negative integer heights.

    Args:
        walls (list): List of non-negative integers representing
                      wall heights.

    Returns:
        int: The total amount of rainwater retained.
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_retained = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, walls[left])
            water_retained += max(0, left_max - walls[left])
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water_retained += max(0, right_max - walls[right])

    return water_retained
