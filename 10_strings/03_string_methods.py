name = "Jothi Annamalai" #strings are immutable

# name[0] = "I" #YOU CANNOT DO THIS ENDS UP IN ERROR


print("Length of the string", len(name)) #space is ommited
print("Upper case String", name.upper())
print("Lower case String", name.lower())
print("capitalized String", name.capitalize())
print("Title String", name.title())

#strip
text = " Hello world " 
print("strip String >", text.strip()) #remove all whitespaces
print("Left strip String >", text.lstrip()) #remove left whitespaces
print("Right strip String > ", text.rstrip()) #remove right whitespaces

#find & replace
text="python is fun"
print("Find Index of first occurance ", text.find("is")) #output: 7 Index of first occurance
print("Replace: ", text.replace("fun", "awesome"))

#split & join
fruits = "apple,banana,mango"
splited_fruits = fruits.split(",")
print("Split: ", splited_fruits)
new_fruits = "-".join(splited_fruits)
print("Join: ", new_fruits)

#Bool return string func
text="Python123"
print("isalpha = ", text.isalpha()) #output: False
print("isdigit = ", text.isdigit()) #output: False
print("isalnum = ", text.isalnum()) #output: True
print("isSpace = ", text.isspace()) #output: False (True if it has only space)