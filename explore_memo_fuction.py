import timeit
from memo import memo

"""Explore using memo function with Fibonacci sequences.
From Python Algorithms by Magnus Lie Hetland, page 176-178
"""

def fib(i):
    """Generate Fibonacci numbers using recursion."""
    if i < 2: return 1
    return fib(i-1) + fib(i-2)

@memo
def fib_cached(i):
    """Generate Fibonacci numbers using recursion and caching values."""
    if i < 2: return 1
    return fib_cached(i-1) + fib_cached(i-2)

# Standard recursion
n = 10
print("The {0}th Fibonacci number is {1}.".format(n, fib(n)))
# n = 100
# print("The {0}th Fibonacci number is {1}.".format(n, fib(n)))

# Recursion with caching
n = 10
print("The {0}th Fibonacci number is {1}.".format(n, fib_cached(n)))
n = 100
print("The {0}th Fibonacci number is {1}.".format(n, fib_cached(n)))