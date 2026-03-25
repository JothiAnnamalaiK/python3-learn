class Employee:
    company = "Vthink"

    def __init__(self, salary, name, bond, company):  # constructor
        self.salary = salary  # create an instance attr of name salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(
            f"The name of employeee is {self.name} . company is {self.company} and  salary is {self.salary} . the bond is for {self.bond} years"
        )


e1 = Employee(34000, "Jothi Annamalai", 2, "Tesla")

print(e1.company)  # will always print instance attr whenever print
e1.get_info()

print("class attr: ", Employee.company)  # prints class attr

# object introspections
print(dir(e1))  # to find all the attr & methods in a obj
