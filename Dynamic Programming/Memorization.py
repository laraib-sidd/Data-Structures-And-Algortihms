"""
Memorization Examples
"""


def add80(num):
    return num + 80


cache = []


def memoizedAdd80(num):
    pass


if __name__ == "__main__":

    print(add80(32))
    print(add80(31))

# Each time we call the function it runs in the momory.
