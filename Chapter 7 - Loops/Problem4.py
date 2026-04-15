# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number. ")

else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number. ")
            break
    else:
        print("Prime number. ")

# for num in range(1, 101):
#     if num >1:
#         for i in range(2, num):
#             if num%2 == 0:
#                 break
#         else:
#             print(num, end=" ")
