"""
2. Getters and Setters
    a.Create a class Employee with a private attribute _salary .
        1. Use @property to define a getter for salary .
        2. Use @salary.setter to prevent setting negative values (print a warning
        instead).
        3. Create an object and test by setting positive and negative salaries.
"""


class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


curr_salary = int(input("Enter your current salary"))
if curr_salary < 0:
    print("Please dont use neg integers for curr. salary")
else:
    e1 = Employee(curr_salary)
    print("Getter curr salary: ", e1.salary)

    exp_salary = int(input("Enter your exp. salary"))
    if exp_salary < 0:
        print("Please dont use neg integers for exp. salary")
    else:
        e1.salary = exp_salary  # setter
        print("Getter Afer setter modify: ", e1.salary)
