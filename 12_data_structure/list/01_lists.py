marks = [85, 96, 78, 56 ,24] #list is an array - mutable
mixed = [85, "Hello", False, 4.2] # this mixed type also valid
extra_marks = [75, 25, 78, 15 ,45]
print(marks[0])

print(marks[0:4])

#List methods
marks.pop() #remove last index
marks.append(63) #this will change the org list
print("pop & append 63 : ", marks)


marks.extend(extra_marks) #kind of array merge
print("extend (arr merge) : ", marks)


marks.insert(1,99) # adding 99 on 1st index
print("insert to 1st index : ", marks)

marks.remove(78) # removing val 78 from list
print("removing the val 78 from list : ", marks)

marks.reverse() #reverse list
print("reverse List : ", marks)

marks.sort() #sort list
print("sort List : ", marks)

marks.sort(reverse=True) # reverse sort list
print("sort List : ", marks)