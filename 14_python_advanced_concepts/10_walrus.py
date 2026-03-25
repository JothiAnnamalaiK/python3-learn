def very_slow_func():
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    return 70


# a = very_slow_func()
if (a := very_slow_func()) > 10:
    print(a)
else:
    print("Its not grt 10")

# walrus operator simply collecting the value into variable
while data := input("Enter value or :q to quit: "):

    if data == ":q":
        break

    print("Entered value is:", data)
