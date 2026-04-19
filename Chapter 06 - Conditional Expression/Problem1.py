# Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter the 1st Number: "))
n2 = int(input("Enter the 2nd Number: "))
n3 = int(input("Enter the 3rd Number: "))
n4 = int(input("Enter the 4th Number: "))

if(n1 > n2 and n1 > n3 and n1 > n4):
    print("The number ", n1, " is greatest number")

elif(n2 > n1 and n2 > n3 and n2 > n4):
    print("The number ", n2, " is greatest number")

elif(n3 > n1 and n3 > n2 and n3 > n4):
    print("The number ", n3, " is greatest number")

else:
    print("The number ", n4, " is greatest number")