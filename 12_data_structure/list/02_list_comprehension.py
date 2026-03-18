# create a list containing the tale of 5

#old method
table=[]
for i in range(1, 11):
    table.append(i*5)
print("old method", table)

# list comprehension method:
tables = [5*i for i in range(1, 11)] #shortcut

print("list comprehension method", tables)

#get square root of 1-10
sq_root = [i**2 for i in range(11)] 

print("square root", sq_root)


#get cube root of 1-10
cube_root = [i**3 for i in range(11)] 

print("cube root", cube_root)