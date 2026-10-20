marks = {"john":34, "jack": 45, "lily": 94}
# print(marks.keys()) #keys are like john etc it will print tht 34 etc are values
# print(marks.values())
# marks.pop("john") #it will remove john and its value
# marks.clear() #it will clear all the elements of dic. only this left {}
# n = marks.fromkeys("marks", 69) #it give random new key
# n = marks.fromkeys(marks, 80) #it give all keys value 80
# marks.items()
# marks.get("john")
# print(marks.keys()) #this will create in tuple form of dict
# print(marks.get("john")) #this give direct value of the key
# marks.popitem() #this will delete the last elemnt whole also its value
# marks.update({"john": 50}) #this update value of john only
# marks.update({"ajijul": 75}) #this will add new key and value
# marks.setdefault("john", 34) #If this key is missing, create it with this default value. Otherwise, leave it alone."
# print(marks.values()) #this give only value
marks.clear() #it clears all the elements of dic
print(marks)