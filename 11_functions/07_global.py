def sum(a, b):
    print("summing 2 nums")
    c = a + b  # local scope

    global z  # to modify the global z
    z = z + 1  # refer to global not local vars
    return c


z = 9
c = sum(3, 5)
print("sum two nums with func: ", c)

print("value of z: ", z)
