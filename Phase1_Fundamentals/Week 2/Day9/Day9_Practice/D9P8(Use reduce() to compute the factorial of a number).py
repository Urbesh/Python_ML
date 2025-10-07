#Use reduce() to compute the factorial of a number
from functools import reduce as red
def factorial_with_reduce(n):
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n==0:
        return 1
    else:
        # reduce applies the lambda function (x*y) cumulatively to the items of the iterable.
        # range(1, n + 1) generates numbers from 1 to n.
        # The initial value for the accumulator is not explicitly provided here,
        # as reduce will correctly handle it by taking the first two elements
        # of the iterable and then accumulating from there.
        return red(lambda x, y: x * y, range(1, n + 1))
number = int(input("Enter any number to know its factorial: "))
result = factorial_with_reduce(number)
print(f"The factorial of {number} is: {result}")
