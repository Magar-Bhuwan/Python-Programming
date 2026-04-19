# Conditional Expressions are use to output the different output with different conditions.
''' Means if the one codition is meet then it gives one output else gives another output.
'''

# For example
''' we have put in order of higher to lower conditions if there are multiple conditions
otherwise it prints first conditions output because it meets that conditions first 
or all conditions.'''

'''
age>=100
age>=60
age>=18
(This gives valid output)

age>=18
age>=60
age>=100
(This gives invalid output because if we put number 67 then it returns age>=18 conditions
output because it comes first and meets conditions)

'''


age = int(input("Enter your age: "))

if(age>=100):
    print("You are too old. ")

elif(age>=60):
    print("You are getting old. ")

elif(age>=18):
    print("You are Young. ")
    print("Good for you. ")

elif(age<0):
    print("Invalid age. ")

elif(age==0):
    print("0 age is not valid. ")

else:
    print("Sorry!")

print("End of the program")


