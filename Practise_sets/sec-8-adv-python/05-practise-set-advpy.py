"""
5. Exception Handling and Custom Errors
    a. Write a program that asks the user to enter a number and handles:
        1. ValueError if the input is not a number
        2. ZeroDivisionError if you try to divide by zero
    b. Create a custom exception NegativeNumberError and raise it when the user
    enters a negative number.
"""


class NegativeNumberError(Exception):
    def __init__(self, message="Do not use negative nums"):
        self.message = message
        super().__init__(self.message)  # passing to base class


while True:

    try:
        number1 = int(input("Enter a number 1: "))
        if number1 < 0:
            raise NegativeNumberError()

        number2 = int(input("Enter a number 2: "))
        if number2 < 0:
            raise NegativeNumberError("Use positive numbers")

        divide = number1 / number2
        print("Divide of num is : ", divide)
    except ValueError:
        print("Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except NegativeNumberError as neg_err:
        print(f"Neg Num Error: {neg_err}")
    except Exception as e:
        print("Some error occured!", e)
