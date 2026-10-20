# q.1
# number = int(input("Enter a number: "))
# if number > 0:
    # print("The number is positive")
# elif number < 0:
    # print("The number is negative")
# else:
    # print("The number is zero")

# q.2
# age = int(input("Enter your age: "))
# if age >= 18:
    # print("You are eligible to vote")
# else:
    # print("You are not eligible to vote")

# q.3

# number = int(input("Enter a number: "))
# if(number % 2 == 0): # this is the condition to check if the number is even or odd it means it divides ur number by 2 and tht why reaminder comes zero
    # print("Even")
# else:
    # print("Odd")

# q.4
# number = int(input("Enter a number: "))
# match number:
    # case 1:
        # print("Sunday")
    # case 2:
        # print("Monday")
    # case 3:
        # print("Tuesday")
    # case 4:
        # print("Wednesday")
    # case 5:
        # print("Thursday")
    # case 6:
        # print("Friday")
    # case 7:
        # print("Saturday")

# q.5
#number_1 = int(input("Enter first number: "))
#number_2 = int(input("Enter second number: "))
#operation = input("Choose operation: ")
#match operation:
    #case "+":
        #print(number_1 + number_2)
    #case "-":
        #print(number_1 - number_2)
    #case "*":
        #print(number_1 * number_2)
    #case "/":
        #print(number_1 / number_2)

# q.6
# for i in range(1,11):
    # print(i)

# q.7
# n = int(input("Enter your number"))
# for i in range(1,11):
    # print(n, "X", i, "=", n*i)

# q.8
# sum = 0
# for i in range(1,101):
    # sum += i
# print(sum)

'''
q.9 print the following pattern 
*
**
***
****
'''

# for i in range(1,5):
    # print("*"*i)

# q.10
# i = 1 
# while i<11:
    # print(i)
    # i = i + 1

# q.11
# password = "dhfdf"
# entered_pass = input("Enter password: ")
# while (entered_pass != password):
    # entered_pass = input("Wrong Password! Try again: ")
# print("Success! You are logged in")

# q.12
# number = 4563
# print(str(number)[::-1]) # so this [::-1]) means string slicing it makes the string from backwards it only applies to string tht why u can see in line 98 we have made it to str

# q.13 
# for i in range(1,11):
    # print(i)
    # if i == 7:
        # break

# q.14
# for i in range(1,11):
    # if i == 5:
        # continue
    # print(i)

# q.15
for i in range(1,6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)