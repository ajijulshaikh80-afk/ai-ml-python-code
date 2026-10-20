# Create a list containing the table of 5
# table = []

# for i in range(1, 11): #this for loop will populate the empty table list
    # table.append(5*i)
# print(table)

#now shortcut method which is list comprehension method
table = [5*i for i in range(1, 11)]
print(table)
