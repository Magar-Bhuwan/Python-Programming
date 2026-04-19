# Write a program to find out whether a student has passed or failed if it
# requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects
# and take marks as an input from the user.


marks1 = int(input("Enter a first marks: "))
marks2 = int(input("Enter a second marks: "))
marks3 = int(input("Enter a third marks: "))

#Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks2))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulation! You are passed. ", total_percentage)

else:
    print("Sorry! You are failed. Try again next year. ", total_percentage)

