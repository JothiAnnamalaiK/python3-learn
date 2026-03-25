z = 8


def sum(a, b):
    # a,b are local scope vars
    c = a + b  # local scope
    return c


z = 9
c = sum(3, 5)
print("sum two nums with func: ", c)

print("value of z: ", z)
