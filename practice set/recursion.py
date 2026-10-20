'''
0 1 1 2 3  5 8 13 # this is Fibonaccci sequence like 1+1=2...
0 1 2 3 4  5 6....

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1) # n-2 means its before to before number
'''

def fib(n):
    # Base case of recursion
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1) # so if u put n=1 or 0 u were getting -ve number which is not in our Fibonaccci so we return tht both value
print(fib(6)) # now this 6 goes to line 13 becomes n then if statament becomes F so now it cames to line 17 and now it becomes see below

fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(5)
0 + 1 + 1 + fib(0) + fib(1) + fib(5)
0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib (1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1

# recursion, a function calls itself and breaks the problem into smaller versions of the same problem, again and again, until it reaches a simple case where it can give a direct answer.

