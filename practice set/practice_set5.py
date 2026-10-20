#q1
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0]) 
# fruits[1] = "orange"
# print(len(fruits))
#q2
# numbers = [i for i in range(1,11)]
# print(numbers[0:3]) 
# print(numbers[7:10])

#q.3
# numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)
# numbers.remove(2)
# print(numbers)

#q.4
# names = ["Alice", "Bob", "Charlie"]
# names.insert(1, "David")
# print(names)

#q.5
# coordinates = (10, 20)
# print(coordinates[0]) 
# print(coordinates[1])

#q.6
# corlist = list(coordinates) #coverting tuple to list
# corlist[0] = 50
# coordinates = tuple(corlist) #coverting list back to tuple
# print(coordinates)

#q.7
# my_set = {1, 2, 3, 3, 4}
# print(my_set)
#q.8
# my_set.add(5)
# my_set.remove(2)
# print(my_set)

#q.9
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.union(b)
# print(c)
# d = a.intersection(b)
# print(d)
# e = b.intersection(a)
# print(e)
# f = a.difference(b)
# print(f)

#q.10
# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])
# student.update({"grade": "A+"})
# student["city"] = "Delhi"
# print(student)

#q.11
# mydict = {"Ajijul": 50505050, "Rohit": 50505051, "Sahil": 50505052}
# mydict.keys()
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

#bonus question
#q.1
# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique_numbers = set(numbers)

# print(unique_numbers)

#q.2
# products = {
    # "Laptop": 50000,
    # "Phone": 30000,
    # "Tablet": 25000,
    # "Headphones": 5000
# }

# highest = max(products, key=products.get)

# print(highest)

#q.3 
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)

print(dict1)