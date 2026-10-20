#positinal argument
# def add(a, b):
    # x = a + b
    # return x


# c = add(3, 5)
# print(c)
# here a and b are called parameters and 3,5 are arguments only difference btw both is tht arguments are real values which are being passed on which computation will take place and parametrs i.e a and b are simply variable names

# Default argument
def add(a, b, plus=0):
    x = a + b + plus
    return x
c = add(3, 5)
print(c)

def add(a, b, plus=0):
    x = a + b + plus
    return x
c = add(3, 5, 2) #so here 2 overides plus 
print(c)
# default arguments are optinal they are wrote at the end of positinal argument

# Keyword arguments
def add(a, b, plus=0):
    x = a + b + plus
    return x
c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3) # we can write arguments in any order this line or thing is called keyword argument in line 26 insie bracket the thing u can see it all should be there when u are making this type of argument

