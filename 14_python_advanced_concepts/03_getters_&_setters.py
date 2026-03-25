class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property  # builtin decorator to use first_name as e.first_name instead of first_name()
    def first_name(self):  # getter
        return self.name.split(" ")[0]

    def last_name(self):  # getter
        return self.name.split(" ")[1]

    @first_name.setter  # builtin decorator to use e.first_name instead of set_first_name()
    def first_name(self, first):  # setter
        l = self.name.split(" ")
        new_fname = f"{first} {l[1]}"
        self.name = new_fname

    def set_last_name(self, last):  # setter
        l = self.name.split(" ")
        new_lname = f"{l[0]} {last}"
        self.name = new_lname


e = Employee("Jothi Annamalai", "36589")

# print("First name: ", e.first_name())
# e.set_first_name("Jo")
# print("Modified First name: ", e.name)


print("First name: ", e.first_name)  # with property decorator
print("Last name: ", e.last_name())  # without property decorator

e.first_name = "Jo"  # with property decorator
print("Modified First name: ", e.name)


e.set_last_name("Anna")  # without property decorator
print("Modified Last name: ", e.name)
