marks = {"harry": 34, "jack": 85, "lilly":94}

print("org_marks", marks, type(marks))

marks["harry"] = 96

print("change harry mark", marks)


#methods
print("get all keys", marks.keys())
print("get all values", marks.values())

marks.pop("lilly")
print("pop", marks)

marks.clear() #clear dictionary
print("clear", marks)




'''
When to Use Each Data Structure?
    DataSt:           Features:            Best For:
    List          Ordered, Mutable     Storing sequences, dynamic data
    Tuple         Ordered, Immutable   Fixed collections, dictionary keys
    Set           Unordered, Unique    Removing duplicates, set operations
    Dictionary    Key-Value Pairs      Fast lookups, structured dat
'''
