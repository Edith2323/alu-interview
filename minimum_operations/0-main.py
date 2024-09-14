#!/usr/bin/python3
"""
Main file for testing the minOperations function.
"""

minOperations = __import__('0-minoperations').minOperations

# Test case 21
n = 21
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

# Test case 19170307
n = 19170307
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

# Test case 972
n = 972
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

# Test case 1 (edge case)
n = 1
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

# Test case 0 (impossible case)
n = 0
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

# Test case -12 (impossible case)
n = -12
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

# Test case 2147483640 (large number)
n = 2147483640
print("Min number of operations to reach {} chars: {}".format(n, minOperations(n)))

