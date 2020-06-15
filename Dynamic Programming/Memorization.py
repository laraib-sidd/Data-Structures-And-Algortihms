"""
Memorization Examples
"""


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


if __name__ == "__main__":

    print(add80(32))
    print(add80(31))
    # Each time we call the function it runs in the momory.

    print(memoizedAdd80(23))
    print(memoizedAdd80(23))
