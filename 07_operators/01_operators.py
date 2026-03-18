a=34
b=2

# 1. Arithmatic operators

print("a + b = ", a + b) #addition
print("a - b = ", a - b) #substract
print("a * b = ", a * b) #multiply
print("a / b = ", a / b) #division
print("a % b = ", a % b) #modules perc
print("a ** b = ", a ** b) #Exponentation
print("a // b = ", a // b) #Floor division

#2. comparative operator

print("is a == b => ", (a == b)) # equals to - True else False
print("is a != b => ", (a != b)) # not equals to - True else False
print("is a < b => ", (a < b)) # less than
print("is a > b => ", (a > b)) # grt than
print("is a <= b => ", (a <= b)) # less than or eql to 
print("is a >= b => ", (a >= b)) # grt than or eql to 


#3. Logical operators
c=True
d=False

'''
True AND True = True
else FALSE on all logic

'''

print(c and c) # True and True
print(c and d) # True and False
print(d and c) # False and True
print(d and d) # False and False


print("Printing not operator...")
print(not(True)) # output: False
print(not(False)) # output: True.


#4. Assignment operators
a=32
print(a)

a*=3
print(a)

#5. Membership operators
fruits = ["apple", "banana", "mango"]

print("banana" in fruits) #True
print("apples" in fruits) #False