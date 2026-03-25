# Imp note:
# `r’ (Read mode): Opens the file for reading. This is the default mode. If the file doesn’t exist, you’ll get an error.


import os

file_path = os.path.join(os.path.dirname(__file__), "user.txt")

"""
    # Method 1
    f = open(file_path, "r")  # r or rt to get in text file mode
    content = f.read()  # put the content into content var
    print(content)
    f.close
"""

# Method 2 using with (Automatically closes file)

try:
    with open(file_path, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Some error occured!", e)
