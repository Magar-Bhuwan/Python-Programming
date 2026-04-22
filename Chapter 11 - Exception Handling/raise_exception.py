# raise exception is use to manually trigger an exception (error) in a program


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

if (a == 0):
    raise ZeroDivisionError ("Zero cannot be divided. ")        # raise calls the exception

else: 
    print(f'Division of number a/b = {a/b}')