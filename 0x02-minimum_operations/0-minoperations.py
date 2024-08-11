#!/usr/bin/python3
def minOperations(n):
    times = 0
    div = 2
    while (n > 1):
        while (n % div == 0):
            n /= div
            times += div
        div += 1
    return times
