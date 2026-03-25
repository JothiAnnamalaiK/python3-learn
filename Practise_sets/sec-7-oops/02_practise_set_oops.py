"""
Q2. Constructor and Attributes
    1. Create a class Person with a constructor ( __init__ ) that accepts name and age
    as arguments and stores them as instance attributes.
    2. Create an object and print the person’s name and age.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Hi {self.name} , and your age is  {self.age}")


p = Person("Jothi Annamalai", 29)

p.details()
