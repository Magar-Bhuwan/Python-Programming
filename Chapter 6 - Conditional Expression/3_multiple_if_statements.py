# We can add multiple if statements in condtional statements.

# For Example:

n = int(input("Enter the age number: "))

# If statement no: 1
if(n%2==0):
    print("The number is Even")
# End of statement no: 1

#If statement no: 2
if(n>=18):
    print("You are above the age of consent. ")

elif(n<0):
    print("Invalid number! ")

else:
    print("You are below the age of consent. ")
# End of statement no: 2

print("Thank You! ")
