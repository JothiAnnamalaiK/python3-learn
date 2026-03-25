# (here custom_exceptions is a folder name)
from custom_exceptions import InvalidAgeError  # custom exception

# class InvalidAgeError(Exception):
#     """custiom exception for invalid age"""  # to view details on hover

#     def __init__(self, message="Age must be above 18 or older!"):
#         self.message = message
#         super().__init__(self.message)  # passing to base class


class Voter:

    def __init__(self, age):
        self.age = age

    def verify_age(self):
        try:
            if self.age < 18:
                raise InvalidAgeError(
                    "Invalid age to vote. Grow first! "
                )  # Raising custom exception (throw err)

            print("Welcome to voters list!")
        except InvalidAgeError as e:
            print(f"Error: {e}")


age = int(input("Enter your age:"))
voter = Voter(age)
voter.verify_age()
