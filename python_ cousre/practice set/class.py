# Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house. e.g form for exam tht contains name,age etc

#object: specific instance created from a template (class) eg. form which contains the data of a specific student like Ajijul

class Employee:
    company = "HP"
    def get_salary(self): #self is e and e2, self is important here cuz self is a way to refernce the object of the class which is being created
        return 34000
#till here it was class

e = Employee() # an object of class Employee is created
print(e.get_salary()) #Employee e's get_salary method is called and it returns 34000

e2 = Employee() 
print(e2.get_salary())
print(e2.company)