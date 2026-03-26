while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        print("Select an operation:")
        print("+ for addition, - for subtraction, * for multiplication, / for division")

        o = input("Enter the operation: ")

        match o:
            case "+":
                print(f"The result of {a} + {b} is: {a + b}")
            case "-":
                print(f"The result of {a} - {b} is: {a - b}")
            case "*":
                print(f"The result of {a} * {b} is: {a * b}")
            case "/":
                print(f"The result of {a} / {b} is: {a / b}")
            case _:
                print("Please select a valid operation.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()
