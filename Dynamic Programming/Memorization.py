"""
Memorization :
It is a way to store a solution to a problem in a memory,
so we don't have to solve the sample problem again.
"""
from functools import lru_cache


def add80(num):
    return num + 80


cache = {}


def memoizedAdd80(num):
    if num in cache:
        return cache[num]
    else:
        print('Long time')
        cache[num] = num + 80
    return cache[num]

# Memoization 2
# https://docs.python.org/3.3/library/functools.html --> Doc for lru_cache


@lru_cache(maxsize=1000)
def memoized2Add80(num):
    return num + 80


if __name__ == "__main__":

    print(add80(32))
    print(add80(31))
    # Each time we call the function it runs in the momory.
    print()
    print(memoizedAdd80(23))
    print(memoizedAdd80(23))
    print()
    # Using python library to create cache
    print(memoized2Add80(54))
    print(memoized2Add80(54))
    print(memoized2Add80.cache_info())
