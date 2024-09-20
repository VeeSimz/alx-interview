#!/usr/bin/python3
""" Making change """


def makeChange(coins, total):
    """ Given coins with different values,
        determine the least number of coins needed to meet a given amount total """
    if total <= 0:
        return 0
    val = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            val[i] = min(val[i], val[i - coin] + 1)
    return val[-1] if val[-1] != float("inf") else -1
