lists = ["Apple", "Elephant", "Cat", "Human", 45, 45.78, "Ram", "Aeroplane"]
print(lists)

lists.append("Sitaram")                             #append("") method --> add in last
print("After Append Lists: ",lists)

lists.insert(6, "Hari")
print("After Insert Lists: ",lists)                 #insert(index number, insert list) method

# lists.pop(5)
print("Delete value: ", lists.pop(5))               #pop(index value) -->delete the data on list
print("After Delete the data on lists: ", lists)

l1 = [5, 3, 6, 7, 9, 1, 90, 30, 27, 78, 45]     
print("Before Sorting: ",l1)
l1.sort()                                           #sort() method --> sorting lists
print("After Sorting: ",l1)

l1.reverse()                                        #reverse() method --> reverse lists
print("Reverse Lists: ", l1)

l1.remove(90)                                       #remove(value) --> removed the value of lists
print("After removed: ", l1)
