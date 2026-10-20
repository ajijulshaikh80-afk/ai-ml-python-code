s = {34, 23, 1, 3, 22}

print(s)
s.add(32) #it can be added in any order
s.add(54)
s.remove(1) #it removes 1 from the set
s.discard(3444) # this only says remove this number if it is in set otherwise dont throw error
# s.remove(3444) #this show error cuz it says only remove the element if present
s.pop() #it removes random element from the set
print(s)