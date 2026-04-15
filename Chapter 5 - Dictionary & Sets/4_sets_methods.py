s = {3, 4, 5, 7, 7, 3, 7, 4, 7, 2}

print(s, type(s))
s.add(13)                          #.add(value) method --> add the value
print(s, type(s))
s.update([3, 8], {6})                #.update() method -->add multiple values
print(s)
s.remove(3)                         #.remove(value) method --> remove values of collection
print(s)
s.discard(5)                        #.discard(value) method --> remove value and if not found then return no errors
print(s)
s.discard(9)                        # 9 value are not there and don't give an error          
print(s)
item = s.pop()                      #.pop(value) method --> removes and returns a random element
print(item) 
print(s)
s.clear()                           #.clear()method -->remove everything of collection values
print(s)

''' Sets Operations 
=====================   '''

a = {1, 2, 3}
b = {2, 3, 4, 5}
print("a = ", a)
print("b = ", b)
print("Union of a & b = ", a.union(b))                          #.union(b) method -->Returns union of sets
print("Intersection of a & B = ", a.intersection(b))            #.intersection(b) method -->Returns common elements of sets
print("Difference = ", a.difference(b))                         #.difference(b) method -->Returns difference elements
print("Symmetric Difference = ", a.symmetric_difference(b))     #.symmetric_difference(b) method -->Returns Elements in either set, but not both
print("Is Subset? = ", a.issubset(b))                           #.issubset(b) method -->Checks if a set is a subset
print("Is Superset? = ", a.issuperset(b))                       #.issuperset(b) method -->Checks if a set is a superset
print("Is disjoint? = ", a.isdisjoint(b))                       #.isdisjoint(b) method -->Checks if sets have no elements in common


