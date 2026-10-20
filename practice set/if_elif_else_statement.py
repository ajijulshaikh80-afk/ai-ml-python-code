age = int(input("Enter your age: "))
#if(age>18):
    #print("You can drive") # 1st statement
#elif(age==18):
   # print("Lets schedule an inetrview") # 2nd statement
#else:
   # print("Sorry you cannot drive") # 3rd statement
# so here each statement is checked one by one if not 1st then 2nd and so on...

if(age <= 50):
    print("You can drive")
elif(age==18):
    print("Lets schedule an inetrview") 
elif(age == 0):
    print("Hey you are just born")
elif(age>50):
    print("You are too old to drive")
else:
    print("Sorry you cannot drive")