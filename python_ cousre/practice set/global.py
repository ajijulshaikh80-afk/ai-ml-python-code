def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z # pls modify global z this line will update the value 
    z = 0 # this will not create local variable
    return c
z = 3
print(sum(3, 12))
print(z)
