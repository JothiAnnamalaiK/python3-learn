def divide(a, b):
    try:
        c = a / b
        print(c)
        return c

    except Exception as e:
        print("Error: ", e)
        return None

    else:  # gets executed if no err in try block
        print("Hey Im good")

    finally:  # executes always even if err in try block
        print("Execution done")


a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))
divide(a, b)
