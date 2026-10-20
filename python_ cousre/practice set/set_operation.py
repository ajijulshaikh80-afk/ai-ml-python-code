a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

# c = a.union(b) #it creats all elements of a and b in c
# print(c)

# d = a.intersection(b) #this will print common elements present in both a and b
# print(d)

# e = a.difference(b) #it gives output which are in a but not in b
f = b.difference(a) #it gives output which are in b but not in a
print(f)