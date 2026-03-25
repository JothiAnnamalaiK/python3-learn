import os

file_path = os.path.join(os.path.dirname(__file__), "jothis.txt")


try:
    with open(file_path, "r") as f:
        for line in f:
            print(line)  # reading line by line if haviung large file to read

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Some error occured!", e)
