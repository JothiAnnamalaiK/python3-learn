names='Jothi Annamalai'

print(names[0:2]) # goes from 0 to 2-1 ie.., 0 to 1

print(names[2:-1]) #start from 2 and strip -1

print(names[0:10:1]) # skip n-1 (1-1) characters
print(names[0:10:2]) # skip n-1 (2-1) characters
print(names[0:10:4]) # skip n-1 (4-1) characters


print(names[:4]) #Replace the first empty number with 0 # same as names[0:4]
print(names[1:]) #Replace the second empty number with length