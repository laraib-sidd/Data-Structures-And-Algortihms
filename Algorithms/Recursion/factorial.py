'''
Write two functions that finds the factorial of any number.
One should use recursive , the other should just use a for loop.
'''


# Recursive
def fact_recursive(number):
    if number == 1:
        return 1
    return number * fact_iterative(number - 1)


# Iterative
def fact_iterative(number):
    if number == 1:
        return 1
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    return fact


# Driver code
if __name__ == "__main__":
    print(fact_iterative(7))
    print(fact_recursive(8))
