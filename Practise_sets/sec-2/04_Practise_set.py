#QA. Basic String Operations:
name="Jothi Annamalai"
'''
    QA_1: Create a string variable name with your full name. Print:
            The first character
            The last character
            The length of the string

    QA_2: Concatenate two strings: "Hello" and "World" with a space in between.
'''
print("Answering QA_1:")

print("first character: ", name[0])
print("last character: ", name[-1])
print("length of string: ", len(name))
print("\n")

print("Answering QA_2:")
print("concat 2 strings: ", "Hello" + " " + "World")
print("\n")



#QB. String Slicing and Indexing:
text = "Python Programming"
'''
    QB_1: Given text = "Python Programming" , do the following:
            Print the first 6 characters
            Print the last 6 characters
            Print every second character from the string

    QB_2: Reverse the string text using slicing.
'''

print("Answering QB_1:")
print("Print the first 6 characters: ", text[0:7])
print("Print the first 6 characters: ", text[:6])
print("Print the LAST 6 characters: ", text[-6:])
print("print every second character from the string: ", text[::2])
print("print every second character from the string: ", text[0:15:2])
print("print even chars: ", text[::2]) #Even positions (0,2,4,...)
print("print odd chars: ", text[1::2]) #Odd positions (1,3,5,...)
print("\n")


print("Answering QB_2:")
print("Reverse the string text using slicing:" , text[::-1]) #reversing the string using slice
print("\n")



#Qc. String Methods and Functions:
text = " i love python programming "
text2="123abc"
'''
    Qc_1: Take the string " i love python programming " and:
            Remove extra spaces from both ends
            Convert it to title case
            Count how many times "o" appears

    Qc_2: Check if the string "123abc" is alphanumeric.
'''

print("Answering Qc_1:")
print("Remove extra spaces from both ends:" , text.strip()) 
print("Remove extra spaces from both ends:" , text.title()) 
print("Count how many times \"o\" appears:" , text.count("o")) 
print("\n")

print("Answering Qc_2:")
print("Check if the string \"123abc\" is alphanumeric:" , text2.isalnum()) 
print("\n")


#Qd.  String Formatting and f-Strings

'''
    Qd_1: Using format() , create a sentence:
            "My name is John and I am 25 years old."
            by passing "John" and 25 as variables.

    Qd_2: Do the same using f-strings.
'''

print("Answering Qd_1:")
name="John"
age=25
template="My name is {} and I am {} years old."

print("Using format() , create a sentence:\n" , template.format(name,age))
print("\n")

print("Answering Qd_2:")
print("Do the same using f-strings:")
print(f"My name is {name} and I am {age} years old.")
print("\n")



#Qe.  String Formatting and f-Strings

'''
    Qe_1: Given sentence = "Coding in Python is fun" , replace "fun" with
"awesome" and print it.

    Qe_2: Find the index of the word "Python" in sentence .
    Qe_3: Convert the entire sentence to uppercase and print it.
'''
sentence = "Coding in Python is fun"

print("Answering Qe_1:")
print("replace \"fun\" with \"awesome\" and print it \n", sentence.replace("fun", "awesome") )
print("\n")

print("Answering Qe_2:")
print("Find the index of the word \"Python\" in sentence", sentence.find("Python"))
print("\n")

print("Answering Qe_3:")
print("Convert the entire sentence to uppercase", sentence.upper())
print("\n")


#Qf.  Bonus Questions
sentences = "Coding in Python is fun"
'''
    Qf_1: Write a program that counts how many vowels are in a given string.

    Qf_2: Take a user input string and check if it is a palindrome (same forwards and
backwards).
'''

print("Answering Qf_1:")
print("counts how many vowels are in a given string")

vowels=["a","e","i","o","u"]
vowels_arr={} #use dictionary (obj) to get output with mapping
for vowel in vowels:
    vowels_arr[vowel] = sentences.count(vowel)

print("New vowels arr: ", vowels_arr)
print("\n")

print("Answering Qf_2:")
print("check if given string it is a palindrome")
string = str(input("Enter your string: "))
rev_str = string[::-1]
print("Yes, Its a palidrome string" if string == rev_str else "No, Its not a palidrome string")


