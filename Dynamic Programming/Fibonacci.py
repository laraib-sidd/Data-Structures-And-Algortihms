"""
Creating the fibonacci program using Dynamic Programming
"""
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib_dp(num):
    if num < 2:
        return num
    else:
        return fib_dp(num - 1) + fib_dp(num - 2)


cache = {}

def fibo(num):
    if num in cache:
        return cache[num]
    elif num > 2:
        cache[num] = num
    else:
        cache[num] = fibo(num - 1) + fibo(num - 2)

    return cache[num]