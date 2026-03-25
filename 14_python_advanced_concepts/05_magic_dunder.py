class Employee:
    company = "Vthink"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Your name is {self.name} and your salary is {self.salary}"

    def __repr__(self):  # mostly used by devloper to show logs
        return f"name: {self.name}\n salary: {self.salary}"

    def __len__(self):
        return len(self.name)


e = Employee("Jothi", 85482)

print("using magic/dunder method using init:", e.name, e.salary)

print("using magic method using Str:", str(e))  # prints __str method

print("using magic method using repr:", repr(e))  # prints __repr__ method

print("using magic method using len:", len(e))
