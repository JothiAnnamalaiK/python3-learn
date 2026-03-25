import os

file_path = os.path.join(os.path.dirname(__file__), "dir")

a = os.listdir(file_path)  # to get the files in dir

print("Listing all files in dirs: ", a)  # list all dir

print("Listing cur working dir", os.getcwd())  # /Users/vt324/vthink-projects/python3

print("Path if exist check:", os.path.exists(file_path))  # True or False


print("Removing sample file")
try:
    rem_file_path = os.path.join(file_path, "sample.txt")
    print("sample file path", rem_file_path)
    os.remove(rem_file_path)  # to remove indiv files
except FileNotFoundError:
    print("No file to remove")


print("Removing whole dir")
# os.rmdir(file_path) #only remove dir if it is empty
