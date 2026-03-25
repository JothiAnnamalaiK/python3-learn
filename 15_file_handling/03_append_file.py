# Imp note:
# ‘a’ (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn’t exist, a new file will be created.


# append to existing file called Jothi.txt
# It should contain addtional data abt Jothi

import os

file_path = os.path.join(os.path.dirname(__file__), "jothis.txt")

'''
    Method 1:
        f = open(file_path, "a")
        string = """
        Jothi is from Apk
        from VNR dist
        """
        f.write(string)
        f.close()

'''

try:
    with open(file_path, "a") as f:
        string = """
        Jothi is from Apk
        from VNR dist
        """
        f.write(string)
        print("File append is success")
except Exception as e:
    print("Some error occured!", e)
