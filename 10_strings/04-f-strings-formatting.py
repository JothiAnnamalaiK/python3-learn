
# string formatting
template = "Dear {}, you are awesome. You won ${}!"

name = "John"
prize = 20000
s1 = template.format(name, prize)
print(s1)

#f strings
print("Using f string..")
print(f"Dear {name}, you are awesome. You won ${prize}!")