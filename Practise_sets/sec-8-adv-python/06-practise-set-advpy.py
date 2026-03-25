from functools import reduce

"""
Q6. map(), filter(), and reduce()
    1. Use map() to convert [1, 2, 3, 4, 5] into their cubes.
    2. Use filter() to get only even numbers from [10, 11, 12, 13, 14] .
    3. Use reduce() from functools to find the product of all elements in [1, 2,
    3, 4] .
"""

# mapping
mapping = [1, 2, 3, 4, 5]
new_map = list(map(lambda x: (x * x * x), mapping))
print("The cubical roots are: ", new_map)


# filtering
filter_nums = [10, 11, 12, 13, 14]
even_filter = list(filter(lambda x: (x % 2 == 0), filter_nums))
odd_filter = list(filter(lambda x: (x % 2 != 0), filter_nums))
print("Even nums: ", even_filter)
print("Odd nums: ", odd_filter)


# reducing
red_nums = [1, 2, 3, 4]

prod_red_nums = reduce(lambda x, y: (x * y), red_nums)

print("prod of all nums using reduce:", prod_red_nums)
