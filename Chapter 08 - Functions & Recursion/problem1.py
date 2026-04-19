#Write a program using functions to find the greatest of three numbers.

def greatest_num(a, b, c):
    if(a > b and a > c):
        print(f"Greatest number is {a} ")
    elif(b > a and b > c):
        print(f"Greatest number is {b} ")
    else:
        print(f"Greatest number is {c} ")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

greatest_num(n1,n2,n3)
        