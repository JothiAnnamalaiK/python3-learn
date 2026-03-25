# Imp note:
# `w’ (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist ,a new file will be created


# write to a file called Jothi.txt
# It should contain data abt Jothi

import os

file_path = os.path.join(os.path.dirname(__file__), "jothi.txt")

'''
    # Method 1
    f = open(file_path, "w")
    string = """
    Jothi is a nice guy
    He is working with Vthink
    """
    f.write(string)
    f.close()
'''

try:
    with open(file_path, "w") as f:
        string = """
        Jothi is a nice guy
        He is working with Vthink
        """
        f.write(string)
        print("File Write is success")
except Exception as e:
    print("Some error occured!", e)
