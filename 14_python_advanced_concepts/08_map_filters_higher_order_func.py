# maps func in python
numbers = [2, 8, 55, 66, 44, 22]


def square(x):
    return x * x


# new_map = list(map(square, numbers))
new_map = list(map(lambda x: (x * x), numbers))  # using lambda
print("Printing maps list values:")
print(new_map)


# filter func in python
def is_grt_9(x):
    if x > 9:
        return True
    else:
        return False


# new_filter = list(filter(is_grt_9, numbers))
new_filter = list(filter(lambda x: x > 9, numbers))
print("Printing filer list values:")
print(new_filter)
