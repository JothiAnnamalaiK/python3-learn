"""
Q3. Static & Class Methods
    a. Create a class MathUtils with:
        1. A @staticmethod called add(a, b) that returns a + b .
        2. A @classmethod called description(cls) that prints "This is a utility class for math operations."
    b. Call both methods without creating an object
"""


class MathUtils:

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return "This is a utility class for math operations"


print("printing desc:", MathUtils.description())
print("adding 2 nums:", MathUtils.add(5, 6))
