# Write a program which finds out whether a given name is present in a list or not.

list_name = ["Ram", "Sita", "Gita", "Hari"]

name = input("Enter your name: ")

if(name in list_name):
    print("Name Lists: ", list_name)
    print("You have entered name: ", name)
    print("Yes, it's present. ")

else:
    print("Name Lists: ", list_name)
    print("You have entered name: ", name)
    print("No, not present. ")

