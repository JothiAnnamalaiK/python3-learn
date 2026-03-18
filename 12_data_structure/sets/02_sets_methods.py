sets = {3,45,85,69}
print("org set: ", sets)


sets.add(32)
print("adding 32 to org set: ", sets) #added to 0th index

sets.remove(3)
print("remove 3 from org set: ", sets) #remove val 3 from org set (if val not exist, will throw err)

sets.discard(88)
print("discard 3 from set: ", sets) #discard val 88 from org set (only if val exist) - no err