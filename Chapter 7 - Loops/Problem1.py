# Write a program to print multiplication table of a given number using for loop

n = int(input("Enter a number of table: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")   #f-string, which allows us to insert the value of name directly in the string.
        
