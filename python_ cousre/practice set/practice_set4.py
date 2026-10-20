# q.1
#def greet():
    #print("Hello, Python Learner!")
#greet()

#q.2
# def square(x):
    # return x*x

# print(square(3))
# print(square(16))
# print(square(21))

#q.3
#def full_name(first, last):
    #return f"{first} {last}"

#print(full_name("Ajijul", "Shaikh"))

#q.4 
# def calulate_area(length, width=10):
    # return  length * width

# print(calulate_area(13, 20))
# print(calulate_area(13))

#q.5
# sum = lambda x, y: x + y
# print(sum(3, 16))

#q.6 create a list [1, 2, 3, 4, 5] and use map() with a lambda fn. to get their squares

# square = lambda x: x*x
# list1 = [1, 2, 3, 4, 5]
# print(list(map(square, list1))) # map takes all numbers

#q.7
'''Write a recursive function factorial(n) that returns the factorial of a number.'''

# def factorial(n):
    # if n == 0 or n == 1:
        # return 1
    # return factorial(n-1) * n # this is factorial formula
# print(factorial(6))

#q.8 Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

# def sum_of_digits(n):
    # if n == 0:
        # return 0
    # return n%10 + sum_of_digits(n//10)

#sum of digits of 7532 is same as:
# 2 (last digit) + sum of digits of 753
# #print(sum_of_digits(7532))

#q.9
# import math
# a = math.sqrt(144)
# b = math.sin(math.radians(90))
# print(a, b)

#q.10
# import requests
# r = requests.get("https://api.github.com")
# print(r.text)

#q.11 Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls

# def increment():
    # counter = 0
    # counter +=1
    # print(counter)

# increment()
# increment()
# increment()
# increment()

#it giving 1 every time as output cuz it local variable it value is not persisted it simply forgot abt all the variables tht are inside this fn.

#q.12 Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

# def multiply(a, b):
'''
    Multiply two numbers.
    Parametrs:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The product of a and b
    '''
    # return a * b

#e.g 
# print(multiply(5, 3))
# print(multiply(2.5, 4))
# help(multiply)

#Bonus q
# q.1 Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
# q.2 Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
# q.3 Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

#q.1
# def fibonacci(n, a=0, b=1):
    # if n == 0:
        # return
    # print(a, end=" ")
    # fibonacci(n - 1, b, a + b)
# fibonacci(7)

#q.2
# def safe_divide(a, b):
    # if b == 0:
        # return "Cannot divide by zero"
    # else:
        # return a / b
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))

#q.3 ans on my_util file
