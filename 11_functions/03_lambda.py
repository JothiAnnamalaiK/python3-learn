# lambda func is used to define inline func in one line

squared = lambda x: x * x
print("lambda squared : ", squared(3))

sum = lambda x, y: x + y
print("lambda sum : ", sum(3, 4))


numbers = [1, 2, 3, 4]
squared_arr = list(map(lambda x: x**2, numbers))
print("squared_arr: ", squared_arr)  # squared_arr
