class Employee:
    company = "Vthink"

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    # instance method (default)
    def print_info(self):
        info = f"Your name is {self.name} and your age is {self.age} and your salary is {self.salary}"
        print(info)

    @staticmethod  # defining the static and ignore passing self and They don’t take self or cls as parameters.
    def sum(a, b):
        return a + b

    @classmethod  # defining its class method
    def print_company(cls):  # cls will refer to the curr class & its attr
        return cls.company

    @classmethod  # defining its class method
    def change_company(cls, new_company):  # cls will refer to the curr class & its attr
        cls.company = new_company

    @classmethod  # can also be used as alternative constructors to create instances of the class in different ways.
    def from_string(cls, data):
        name, salary, age = data.split("-")
        return cls(name, int(salary), int(age))  # Creates a new Person instan


e1 = Employee("Jothi", 36995, 29)
e2 = Employee("Annamalai", 85952, 30)

e1.print_info()
e2.print_info()

print("class attr company: ", Employee.company)


print("sum of 2 nums using static class:", e2.sum(4, 5))

print("using class method printing org comp name:", e1.print_company())

e1.change_company("Accenture")  # changing the class variable here using class method

print("using class method printing modified comp name:", Employee.company)


p = Employee.from_string("JothiAnnamalai-25899-29")
print(p.name, p.salary, p.age)  # JothiAnnamalai 29
