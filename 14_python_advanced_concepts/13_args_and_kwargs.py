# Basic usage of agrs
def sum(a, b):
    return a + b


print(sum(3, 2))  # 5

# print(sum(3, 2, 5))  # gives err becoz of invalid arg count


# using *agrs to use multiple args
def sums(*args):
    # print(args)  # args will be a tuples
    total = 0
    for items in args:
        total += items
    return total


print("Printing multiple args:")
print(sums(3, 2, 5, 360))


# using *kwargs
def marks(**kwargs):
    # kwargs is the dictionary with all the key-value pairs which were passed into marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")


print("Printing usage of kwargs:")
marks(Jothi=75, Vijay=89, jojo=90, vivi=23)


# using both *args and **kwargs together
def func1(*args, **kwargs):
    print("Printing usage of args & kwargs together:")
    print("args: ", args)
    print("kwargs:", kwargs)


func1(1, 2, 3, 4, jack=53, jill=89, kjo=33)
# output:
# args:  (1, 2, 3, 4)
# kwargs: {'jack': 53, 'jill': 89, 'kjo': 33}
