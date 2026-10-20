# string formatting

template = "Dear {}, You are awesome. Take this {}$ bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

# s1 = template.format(a, a1)
# print(s1)
# s2 = template.format(c, c2)
# print(s2)

# another way of formatting strings is using f-strings which is available in python 3.6 and above it is better method
print(f"{a} you are awesome and take this {a1}$ bag")