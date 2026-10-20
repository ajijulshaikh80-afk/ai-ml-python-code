# name = "Ajijul" # strings are immutable in python means you cannot change the value of a string once it is created. You can only create a new string with the desired changes.
# name[0] = "R" # you cannot do this
# a = len(name) # len means length of the string it is a function
# print(a)

# s = "hello world"
# a = len(s) # here in the string "hello world" the length is 11 because there are 11 characters in the string including the space.
# print(a)

# s = "hello world"
# a = len(s) 
# print(a)
# print(s.upper()) # this will print the string in uppercase all letters
# print(s.lower()) # this will print the string in lowercase all letters
# print(s.capitalize()) # this will print the string with the first letter capitalized and the rest in lowercase
# print(s.title()) # this will print the string with the first letter of each word capitalized

# text = " hello world "
# print(text.strip()) # this removes the whitespace from the beginning and end of the string only not from the middle 
# print(text.lstrip()) # this removes the whitespace from only left side of the string
# print(text.rstrip()) # this removes the whitespace from only right side of the string

# text = "Python is fun"
# print(text.find("fun")) # this will tell position of the word "fun" specifically the first letter of the word
# print(text.replace("fun", "easy")) # this will replace the word "fun" with "easy" in the string

text = "Apples,Bananas,Pineapples"
print(text.split(",")) # this will split the string into a list of strings 
print(",".join(['Apples', 'Bananas', 'Pineapples'])) # this will join the list of strings into a single string this will become Apples,Bananas,Pineapples because we are joining the list with a comma

text = "Python123"
print(text.isalpha()) # it checks if all the characters in the string are alphabets or not it will return True or False
print(text.isdigit()) # it checks if all the characters in the string are digits or not
print(text.isalnum()) # it checks if all the characters in the string are alphanumeric or not
print(text.isspace()) # it checks if it only contains whitespace only and ntg else " " and "\t" and "\n" are considered whitespace characters tht why they give output true

 