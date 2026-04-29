# Write a program to input name, marks and phone number of a student and format it using format 
# function like below:
# " The name of student is Harry, his marks are 75 and phone number is 9999999999 "


name = input("Enter the name of the student: ")
marks = input("Enter the marks of the student: ")
phone_number = input("Entet the phone number of the student: ")

format_string = "The name of student is {0}, his marks are {1} and phone number is {2}".format(name, marks, phone_number)
print(format_string)