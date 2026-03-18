a = {23, 4, 5, 6 ,67}

b = {4, 67, 23, 36 ,72}

# UNION:
c= a.union(b) # union a and b with out duplications
print("union sets: ", c) # output: {67, 4, 5, 6, 36, 72, 23}
print("union sets with sort: ", sorted(c)) # output:  [4, 5, 6, 23, 36, 67, 72]

#INTERSECTIONS:
d= a.intersection(b) # intersection a and b with out duplications
print("intersection sets: ", d) # output: {67, 4, 23}
print("intersection sets with sort: ", sorted(d)) # output: [4, 23, 67]

#DIFFERENCES:
e= a.difference(b) # difference a and b with out duplications
print("difference sets: ", e) # output: {5, 6}
print("difference sets with sort: ", sorted(e)) # output: [5, 6]