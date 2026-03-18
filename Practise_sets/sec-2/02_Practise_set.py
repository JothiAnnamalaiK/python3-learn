#Q1. Write a program that prints:
'''
    Hello, World! Welcome to Python.
'''
print("Answering Q1:")
print("Hello, World! Welcome to Python.")

print("\n")

#Q1. Write a program that prints the following poem using a single print() statement:
'''
    Twinkle, twinkle, little star,
    How I wonder what you are!
'''

print("Answering Q2:")
print("Twinkle, twinkle, little star,\nHow I wonder what you are!")
print("\n")

#Q3. Variables & Data Types:
'''
    Create variables to store: - Your name (string)
    - Your age (integer)
    - Your height in meters (float)
    - A boolean value representing whether you are a student
    Print all of them in one line
'''

# print("Answering Q3:")
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in metres: "))
# is_student = input("Type Y if you are a student else N ")
# std_str = "also a student" if is_student.upper() == 'Y' else "not a student" #ternary

# print(f"Candidate Name is {name} and age is {age} and height is {height} metres and {std_str}")
# print("\n")



#Q4. Typecasting Practice:
'''
   You are given a string:
   num = "45"
   Convert it into an integer and add 10 to it. Print the result.
'''
print("Answering Q4:")
num = "45"
num1 = int(45)
print("adding 10 to int 45", num1+10)
print("\n")

#Q5. Taking User Input:
'''
    Write a program that:
        Asks the user for their favorite food.
        Prints: Wow! I also like <food>.
'''

print("Answering Q5:")
# fav_food = str(input("Enter your fav food: "))
# print(f"Wow! I also like {fav_food}", end="!")
# print("\n")


#Q6.Simple Calculator:
'''
    Write a program that:
        Takes two numbers as input from the user.
        Print: Prints their sum, difference, product, and quotient.
'''

print("Answering Q6:")
# num_1 = int(input("Enter your 1st num: "))
# num_2 = int(input("Enter your 2nd num: "))

# print("Sum of 2 Nums are", num_1 + num_2)
# print("Diff of 2 Nums are", num_1 - num_2)
# print("Product of 2 Nums are", num_1 * num_2)
# print("Quotient of 2 Nums are", num_1 / num_2)
# print("\n")


#Q7.Escape Sequences:
'''
    Print the following output using escape sequences:
        Harry said, "Python is awesome!"
        This is on a new line.
        This is a tab -> <- here
'''

print("Answering Q7:")
print("Harry said, \"Python is awesome!\"\n" \
"This is on a new line.\n" \
"This is a tab \t here")
print("\n")

#Q8.Operator Challenge:
'''
    Write a program that:
        Takes an integer as input from the user.
        Prints the square and cube of that number.
        
'''
print("Answering Q8:")
# num = int(input("Enter your 1st num: "))
# print("Square of 2 Nums are", num ** 2) #SQUARE ROOT
# print("cube of 2 Nums are", num ** 3) #CUBIC ROOT
# print("\n")

#Q9.Quick Quiz (True/False):
'''
   Mark True or False:
        Python code must always end with a semicolon ; .
        The # symbol is used for comments in Python.
        "123" and 123 are the same in Python.
        The * operator is used for multiplication.
        \n creates a new line.
        Variables in Python can start with numbers.
        int("10") + 5 gives 15 .
        
'''
print("Answering Q9:")
print("Whether Python code must always end with a semicolon ; => ", True)
print("Whether The # symbol is used for comments in Python. => ", True)
print("Whether  \"123\" and 123 are the same in Python. => ",  False)
print("Whether The * operator is used for multiplication. => ", True)
print("Whether \\n creates a new line. => ", True)
print("Whether Variables in Python can start with numbers. => ", False)
print("Whether int(\"10\") + 5 gives 15 . => ", True)
print("\n")