#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations"""
    times = 0
    div = 2
    while (n > 1):
        while (n % div == 0):
            n /= div
            times += div
        div += 1
    return times
