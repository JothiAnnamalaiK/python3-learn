"""
7. Walrus Operator
    1. Use the walrus operator to read input until the user enters "quit" . Print each
    input as it is entered.

    2. Use the walrus operator in a list comprehension to store lengths of words
    from ["python", "rocks", "ai"] in a list while filtering out words shorter
    than 4 characters
"""

print("Answering Q7-1")
while string := input("Enter a string or type :q to quit: "):
    if string == ":q":
        break

    print("Entered string is : ", string)


print("Answering Q7-2")
result = list(
    filter(lambda x: (len(x) < 4), len_of_words := ["python", "rocks", "ai", "joe"])
)

print("List of words: ", len_of_words)
print("Printing words less than 4 chars:", result)
