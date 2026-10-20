#x = 10
#y = 5
#print(f"The sum of {x} and {y} is {x + y}")

# formatting numbers
#pi = 3.14159265
#print(f"Pi rounded to 2 decimal places is {pi:.2f}") # here {pi:.2f} means pi the value we want to print, : means formatting statrs here, .2 means show 2 digits after the decimal point, f means floating point number

# padding and alignment
text = "Python"
print(f"{text:>10}") # Right align as text has six characters and we are giving 10 so 10-6 = 4 spaces will be added to the left of the text to make it right aligned
print(f"{text:<10}") # Left align 10-6=4 spaces will be added to the right of the text to make it left aligned

print(f"{text:^10}") # Center align means 10-6=4 spaces will be added to the left and right of the text to make it center aligned

#Padding means adding extra spaces (or sometimes other characters) around a value to make it a certain width/length.

#Aligment means positioning the value within that width/length, either to the left, right, or center.