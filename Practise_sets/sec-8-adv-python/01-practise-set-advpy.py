"""
Q1. Decorators in Python:

    a. Write a decorator logger that prints "Function is being called" before
    the function runs. Use it to decorate a function say_hello() that prints
    "Hello!" .

    b. Write a decorator timer that calculates how long a function takes to execute.
    Test it with a function that sums numbers from 1 to 1,000,000.
"""


def mydecorator(func):
    def wrapper():
        print("Function is being called...")
        func()

    return wrapper


@mydecorator
def say_hello():
    print("Executing Q1 a")
    print("Hello!")


say_hello()


"""
b. Write a decorator timer that calculates how long a function takes to execute.
    Test it with a function that sums numbers from 1 to 1,000,000.
"""

from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        # print(f"{func.__name__} took {end - start:.6f} seconds")
        print(f"{func} took {end - start:.6f} seconds")  # if use @wraps from functools

        return result

    return wrapper


@timer
def sum_one_million(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


result = sum_one_million(1000000)
print("Sum one million:", result)
