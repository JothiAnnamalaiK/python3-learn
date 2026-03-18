#QA. If-Else Conditional Statements:
'''
    QA_1: Write a program that asks the user for a number and prints whether it is
positive, negative, or zero
'''
print("Answering QA_1:")

# num = int(input("Enter a number to check: ")) 
# if num < 0:
#     print(f"The given number {num} is Negative")
# elif num > 0:
#     print(f"The given number {num} is positive")
# else: 
#     print("Number is zero")

# print("\n")


'''
    QA_2: Create a program that checks if a person is eligible to vote (age >= 18)
'''
print("Answering QA_2:")

# age = int(input("Enter your age: ")) 
# if age > 18:
#     print("Congrats!!.. You are eligible for voting!!!")
# elif age == 18:
#     print("Get voter ID first")
# else: 
#     print("Not eligible for voting!!")

# print("\n")


'''
    QA_3: Write a program that takes a number from the user and prints “Even” if it is
even, otherwise “Odd”.
'''
print("Answering QA_3:")

# number = int(input("Enter the number: ")) 
# print("Even Number" if number % 2 == 0 else "Odd Number")
# print("\n")



#Qb. Match Case Statements:

'''
    Qb_1: Ask the user to enter a day number (1–7) and print the corresponding day of
the week using match case .
'''
print("Answering Qb_1:")

# num = int(input("Enter the day number (1-7): ")) 

# match(num):
#     case 1:
#         print("The day is Sunday")
#     case 2:
#         print("The day is monday")
#     case 3:
#         print("The day is tuesday")
#     case 4:
#         print("The day is wednesday")
#     case 5:
#         print("The day is thursday")
#     case 6:
#         print("The day is friday")
#     case 7:
#         print("The day is saturday")
#     case _:
#         print("Enter the day number only from (1–7)")

# print("\n")


'''
    Qb_2: Write a program using match case that simulates a simple calculator.
        Ask the user for two numbers and an operation (+, -, *, /).
        Perform the operation using match case .
'''

print("Answering Qb_2:")
# num1 = int(input("Enter the 1st number: ")) 
# num2 = int(input("Enter the 2nd number: ")) 
# operation=str(input("Enter the operation ilike +,-,*,/,%,**,// "))

# match(operation):
#     case '+':
#         print(f"The sum of {num1} and {num2} is ", num1+num2)
#     case '-':
#         print(f"The diff of {num1} and {num2} is ", num1-num2)
#     case '*':
#         print(f"The multiply of {num1} and {num2} is ", num1*num2)
#     case '/':
#         print(f"The divide of {num1} and {num2} is ", num1/num2)
#     case '%':
#         print(f"The percent of {num1} and {num2} is ", num1%num2)
#     case '**':
#         print(f"The power of {num1} and {num2} is ", num1**num2)
#     case '//':
#         print(f"The div of {num1} and {num2} is ", num1//num2)
#     case _:
#         print("The operator is invalid")
# print("\n")



#Qc. For Loops Statements:

'''
    Qc_1:   a.Print numbers from 1 to 10 using a for loop.
            b.Print the multiplication table of a number (entered by user).
            c.Calculate the sum of all numbers from 1 to 100 using a for loop.
            d.Print the following pattern using a for loop:
            *
            **
            ***
            ****
'''


print("Answering Qc_1a:")

print("Printing num from 1-10")
for i in range(1,11):
    print(i)
print("\n")



print("Answering Qc_1b:")

# print("Printing multiply of user given number")
# num = int(input("Enter the number to multiply with: "))
# for i in range(1,11): 
#     print(f"The multiply of {i} x {num} = ", i*num )
# print("\n")


print("Answering Qc_1c:")

print("calculating the sum of all numbers from 1 to 100")
sum=0
for i in range(1,101): 
    sum+=i
print("The sum of all numbers from 1 to 100 is ", sum)
print("\n")


print("Answering Qc_1d:")

print("Print the following pattern")

for i in range(1,5): 
    print("*" * i)
print("\n")





#Qd. While Loops Statements:

'''
    Qd_1:   a.Print numbers from 1 to 10 using a while loop.
            b.Write a program that keeps asking the user to enter a password until they
            enter the correct one.
            c.Use a while loop to reverse a given number (e.g., 123 → 321).
'''


print("Answering Qd_1a:")
print("Printing num from 1-10 while")
i=1
while(i <= 10):
    print(i)
    i+=1
print("\n")


print("Answering Qd_2a:")
# print("Write a program that keeps asking the user to enter a password until they enter the correct one.")

# curr_pass="123456"
# password=input("Enter your password: ");
# while(password != curr_pass):
#     print("Invalid Password. Please try again")
#     password=input("Enter your password: ");

# print("Password is correct!!")
# print("\n")

print("Answering Qd_2a:")
# print("Use a while loop to reverse a given number (e.g., 123 → 321)")

# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10          # get last digit
#     reverse = reverse * 10 + digit
#     num = num // 10           # remove last digit

# print("Reversed number:", reverse)



#Qe. Break, Continue, and Pass Statements:

'''
    Qe_1:   a.Use a for loop to print numbers from 1 to 10, but stop the loop if the
            number is 7 (use break ).
            b.Print numbers from 1 to 10, skipping the number 5 (use continue ).
            c.Write a loop that goes through numbers 1 to 5, but does nothing for number
            3 (use pass ).
'''


print("Answering Qe_1a:")
print("Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break )")

for i in range(1,11):
    print(i)
    if(i==7):
        break

print("\n")



print("Answering Qe_1b:")
print("Print numbers from 1 to 10, skipping the number 5 (use continue)")

for i in range(1,11):
    if(i==5):
        continue
    print(i)

print("\n")

print("Answering Qe_1c:")
print("Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass )")

for i in range(1,6):
    if(i==3):
        pass
    print(i)

print("\n")