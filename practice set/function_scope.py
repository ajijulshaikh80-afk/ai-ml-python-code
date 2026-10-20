def sum(a, b):
    c = a+ b # a and b are local variables it means you can only access these variables inside a fn. u cant access them outside the fn.
    z = 1 # this doesnt chnage the z =8 value cuz it creates a local varible called z which is destroyed after this fn. returns
    return c

def greet():
    z = 32 # local variable
    print("Hello")

z = 8 # z is a global variable u can access it anywhere in program
print(z)
print(sum(4, 6)) # this 4,6 is passed to a,b and c becomes 10 and c is return and this means a b c are wiped out of memory and tht how fn. work

# global varible are those which are outside of fn. not inside
