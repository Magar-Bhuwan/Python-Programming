marks = {
    "Ramlal": 95,
    "Rohan": 91,
    "Yaman": 97,
}
print(marks)
print(marks.items())                        #.items() method  -->Returns a list of (key,value) tuples
print(marks.keys())                         #.keys() method  -->Returns a list of keys tuples
print(marks.values())                       #.values() method  -->Returns a list of values tuples
marks.update({"Rohan": 90, "Pradip": 84})   #.update({" ": }) method - Update the list of keys and values
print(marks)

print(marks.get("Ramlal"))                  #.get(" ") method -->Returns the value of the specified keys and if not found then return None
print(marks["Ramlal"])                      #It returns also value but if not found then it gives an errors
print(marks.clear())                        #Clear everything/None
print(marks.pop("Ramlal", "100"))           #Remove the specified key and returns the corresponding value.
# last_item = marks.popitem()                   #.popitem() method --> remove last items of list
# print("Removed item: ", last_item)
# print("Remaining dictionary: ", marks)
