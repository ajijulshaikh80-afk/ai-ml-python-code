#a = 4
#b = 2
# c = 1
# average = (a + b + c)/3
# print(average)

# if we want to make change then we have to make changes there aslo where we have copy pasted tht we want a thing where if we do only chnage in one place it will work and tht is function

def average(a, b, c): # to make a function we have to write first def it the keyword
    d = (a + b + c)/3.0
    #print(d)
    return d
o1 = average(3, 5, 1) # this value will be passed to a,b,c
o2 = average(4, 6, 1)
print(o1) # so output coming none as no value is assigned to o1 and o2 so tht why we put return which will now assign d value to o1 and o2 return is a keyword just like def in python
print(o2)

