class Employee:
    def __init__(self, salary, name, bond):  # constructor
        self.salary = salary  # create an instance attr of name salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(
            f"The name of employeee is {self.name} . salary is {self.salary} . the bond is for {self.bond} years"
        )


e1 = Employee(34000, "Jothi Annamalai", 2)

e1.get_info()
