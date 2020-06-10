'''Implement a function that reverses a string using iteration...
and then recursion!'''


# Iterative
def iter_reverseString(str):

    if str or str > 2:
        str = list(str)
        str = str[::-1]
        str = "".join(str)
        print(str)
        return True
    else:
        print("Incorrect Input")


# Recursive
def recur_reverseStrign(str):
    pass


if __name__ == "__main__":
    iter_reverseString('My iterative example')
    recur_reverseStrign('My recursive example')
