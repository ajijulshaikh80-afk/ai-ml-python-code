class Employee:
    def __init__(self, salary, name, bond): #_init_ is a constructor which is used to initialize the attributes of the object
        self.salary = salary #creates an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")
    
e1 = Employee(34000, "Jack", 4)
print(e1.get_salary())
e1.get_info()

#So why do we need __init__()?
'''Think:
Without __init__:
Create object → manually give it data
With __init__:
Create object → __init__ automatically sets its data'''



'''Without __init__
First create an empty student:
class Student:
    pass

s1 = Student()
Now the student is empty. Then you fill in the details:
s1.name = "Rohan"
s1.age = 18
So:
Create → Fill details
With __init__
You give the details while creating the student:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rohan", 18)
So:
Create + Fill details together'''