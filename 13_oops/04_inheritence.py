class Animal:  # Parent class (superclass)
    location = "Chennai"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("speaking now...")


class Dog(Animal):  # this is how inheritence done in python
    def speak(self):  # method overriding
        super().speak()  # calling parent class method using super keyword
        print("bow bow!")


# a = Animal("Dog")
# a.speak()


d = Dog("Bruno")
d.speak()

print("Location: ", d.location)
