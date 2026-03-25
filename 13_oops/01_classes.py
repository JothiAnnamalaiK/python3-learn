# class= class is a blueprint or a templete.
# For ex: Form for an exam that contains name , age, electives, father's name etc..,

# object : specific instance created from the template
# Eg: form which contain the data for the student


class Employee:
    company = "Vthink"

    def get_salary(self):  # self is imp becoz its a way to ref the obj of class created
        return 34000


e1 = Employee()  # an instance of class employee is created
print("e1 salary: ", e1.get_salary())  # employees get salary methos is called

e2 = Employee()
print("e2 salary-company: ", e2.get_salary(), "-", e2.company)
