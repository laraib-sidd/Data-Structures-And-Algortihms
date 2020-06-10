'''
Given a number N return the index value of the Fibonacci sequence,
where the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
the pattern of the sequence is that each value is
the sum of the 2 previous values, that means that for N=5 → 2+3

For example: fibonacciRecursive(6) should return 8
'''


def fibo_recursive(num):
    if num < 2:
        return num
    return fibo_recursive(num - 1) + fibo_recursive(num - 2)


def fibo_iterative(num):
    a = 0
    b = 1
    sum = 0
    for i in range(0, num):
        sum = a + b
        a = b
        b = sum
    return sum


# Driver code
if __name__ == "__main__":
    print(f"Recursion : {fibo_recursive(8)}")
    print(f"Iterative : {fibo_iterative(8)}")
