"""
Q8. *args and **kwargs
    1. Write a function sum_all(*args) that accepts any number of integers and
    returns their sum.

    2. Write a function print_details(**kwargs) that prints key-value pairs passed
    as arguments, for example:

        print_details(name="Alice", age=25, city="Delhi")
        # Output:
        # name: Alice
        # age: 25
        # city: Delhi
"""

print("Answering Q8-1")


def sum_all(*args):
    total = 0
    for arg in args:
        total += arg

    return total


print("The sum of given num is", sum_all(22, 33, 66))


print("Answering Q8-2")


def print_details(**kwargs):
    for item in kwargs.keys():
        print(f"{item} : {kwargs[item]}")


print("Printing Kwargs...")
print_details(name="Alice", age=25, city="Delhi")
