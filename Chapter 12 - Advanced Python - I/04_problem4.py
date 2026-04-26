# Write a program to find a/b where a and b are integers. If b == 0, display infinite by handling "ZeroDivisionError"


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a/b)
    
except ZeroDivisionError as e:
    print("Infinite error")
