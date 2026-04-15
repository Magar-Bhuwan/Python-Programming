# if: elif: else: ladder
# This type of conditionals are use to multiple conditions checks and output the different results

# Example: if(marks>=80, "Distinction"), if(marks>=60, "First"), if(marks>=45, "Second"),
# if(marks>=32, "Third"), if(marks<32, "Fail")

marks = int(input("Enter your marks: "))

if(marks>100):                                  #if condition is true then executes
    print("Cannot be marks above 100! ")        

elif(marks>=80):
    print("Distinction. ")

elif(marks>=60):
    print("First. ")

elif(marks>=45):
    print("Second. ")

elif(marks>=32):
    print("Third. ")

elif(marks>=0):
    print("Fail. ")

else:
    print("Invalid marks! ")

print("Thank you! ")