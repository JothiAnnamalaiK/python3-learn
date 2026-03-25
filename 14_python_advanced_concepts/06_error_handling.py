while True:
    a = int(input("Enter 1st num:"))
    b = int(input("Enter 2nd num:"))

    if a == 0 or b == 0:
        raise ValueError("Do not use zero while divide")

    try:
        print(f"The DIV of this nums are : {a/b}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print("Some error occured!", e)
