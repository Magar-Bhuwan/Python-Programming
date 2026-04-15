# Write a program to calculate the grade of a student from his marks from the following scheme:

'''
90 - 100 => A+
80 - 90 => A
70 - 80 => B
60 - 70 => C
50 - 60 => D
<50 => E
'''

subject1 = int(input("Enter a marks of subject1: "))
subject2 = int(input("Enter a marks of subject2: "))
subject3 = int(input("Enter a marks of subject3: "))
subject4 = int(input("Enter a marks of subject4: "))
subject5 = int(input("Enter a marks of subject5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total_marks/5
print("\nTotal Marks: ", total_marks)
print("Percentage: ", percentage)

if(percentage<=100 and percentage>=90):
    print("Grade: A+ ")              # grade = "A+"

elif(percentage>=80):
    print("Grade: A ")              # grade = "A"

elif(percentage>=70):
    print("Grade: B ")              # grade = "B"

elif(percentage>=60):
    print("Grade: C ")              # grade = "C"

elif(percentage>=50):
    print("Grade: D ")              # grade = "D"

elif(percentage<50):
    print("Grade: E ")              # grade = "E"

#print("Grade: ", grade)

