"""
Q1. Create a Simple Class and Object
    1. Create a class Car with a method drive() that prints "Car is moving" .
    2. Create an object of Car and call drive() .
"""


class Car:
    def drive(self):
        return "Car is moving"


car = Car()
obj = car.drive()
print("car drive status: ", obj)
