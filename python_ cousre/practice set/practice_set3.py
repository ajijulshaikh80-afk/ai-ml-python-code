#Q.1
##name = "Ajijul Shaikh"
#print(name[0])
#print(name[-1])
#print(len(name))

#q.2
#str1 = "Hello"
#str2 = "World"
#print(str1 + " " + str2) # this will print Hello World
#or
#print(str1,str2) # this will print Hello World but here space is added by default

#q.3
#text = "Python Programming"
#(text[0:6]) # this will print Python
#print(text[12:19]) # OR ANOTHER WAY
# print(text[-6:]) 
# print(text[0:19:2]) #or another way print(text[::2]) 
# print(text[::-1]) # this will print the whole string in reverse order

#q.4
# text = "  i love python programming  "
# print(text.strip()) # this will remove the spaces from the start and end of the string
# print(text.title()) # this will convert the first character of each word to uppercase
# print(text.count("o")) # this will count the number of times "o" is present in the string new thing

#q.5
# str1 = "123abc"
# print(str1.isalnum()) 

#q.6
# template = "My name is {} and I am {} years old."
# a = "John"
# a1 = 25
# print(template.format(a, a1))
# print(f"My name is {a} and I am {a1} years old.")

#q.7
# sentence = "Coding in Python is fun"
# print(sentence.replace("fun", "awesome"))
# print(sentence.find("Python"))
# print(sentence.upper())

#Bonus Question
#q.8  Write a program tht counts how many vowels are in a given string
# sentence = "Coding in Python is fun"
# sum = 0
# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in sentence: # here u can write for char in sentence.lower(): as this will convert whole sentence in small so tht any capital vowel will not be miss out
    # if(char in vowels): # these two lines means if this character is a vowel increse the vowel count by 1
        # sum += 1
# print(f"There are {sum} vowels in this sentence")

#q.9 Take a user input string and check if it is palindrome(means same as fowrad and backwaerd)

string1 = "madam"
if(string1 == string1[::-1]):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")

# End of bonus q and set





