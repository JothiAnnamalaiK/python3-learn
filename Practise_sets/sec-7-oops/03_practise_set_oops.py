"""
Q3. Simple Inheritance
    1. Create a base class Animal with a method sound() that prints "Some sound" .
    2. Create a derived class Dog that overrides sound() to print "Bark!" .
    3. Create an object of Dog and call sound() .
"""


class Animal:
    def sound(self):
        print("Speaking now from parent..")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark Bow bow!")


d = Dog()

d.sound()
