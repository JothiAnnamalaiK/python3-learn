# reduce func in python:
from functools import reduce  # need to import from inbuild

red_nums = [1, 2, 3, 4, 5, 6]
#          [3,3,4,5,6]
#          [6,4,5,6]
#          [10,5,6]
#          [15,6]
#          [21] #this is how it works with reduce


def sum(a, b):
    return a + b


c = reduce(sum, red_nums)

print("Printing reduce values:")
print(c)
