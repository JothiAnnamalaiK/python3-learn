# position & default arg
def add(a, b, plus=0):
    return a + b + plus


c = add(3, 5, 2)
print("adding two nums with func: ", c)


# keyword arguments
def students(name, age):
    print(f"Hi {name}, and your age is {age}")


students(age=29, name="Jothi Annamalai")
