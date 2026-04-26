# Write a list comprehension to print a list contains the multiplication table of a user entered number.

n = int(input("Enter a number for multiplication: "))

multiplication = [i*n for i in range(1,11)]
# print(multiplication)
for i, result in enumerate(multiplication, 1):
    print(f"{n} x {i} = {result}")
