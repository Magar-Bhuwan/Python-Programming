# Write a program to print the following star pattern.
'''
    *
   ***
  *****
for n = 3
'''
# n = int(input("Enter the number: "))
# for i in range(1, n+1):                 #loop run from i=1 to i=n
#     print(" "* (n-i), end="")           #print spaces (n - i) / end="" means the cursor stays on the same line instead of moving the next line.
#     print("*"* (2 * i - 1), end="")     #the pattern creates odd numbers: 1, 3, 5, 7, 9.
#     print("")                           #just prints an empty string -> moves the cursor to the next line.
    

'''
    *
   ***
  *****
for n = 3
'''


n = int(input("Enter a number: "))

for i in range(1, n+1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


'''
  reverse the pattern:

  *****
   ***
    *

  '''

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

'''
  diamond pattern:

    *
   ***
  *****
   ***
    *

  '''

n = int(input("Enter a number: "))

for i in range(n):
    spaces = n - i + 1
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

for i in range(n-2, -1, -1):
    spaces = n - i + 1
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

'''
  reversed diamond pattern:

  *****
   ***
    *
   ***
  *****

  '''

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    spaces = n - i 
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

for i in range(2, n+1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


'''
  corner pattern:

  *
  ***
  *****
  ***
  *

  '''
n = int(input("Enter a number: "))

for i in range(n):
    stars = 2 * i - 1
    print("*" * stars)
for i in range(n-2, -1, -1):
    stars = 2 * i - 1
    print("*" * stars)


'''
for n = 3
   
*****
  ***
    *

'''
n = int(input("Enter a number: "))

for i in range(n):
    spaces = 2 * i
    stars = 2 * (n - i) - 1
    print(" " * spaces + "*" * stars)

'''
for n = 3

    *
  ***
*****

'''
n = int(input("Enter a number: "))

for i in range(n):
    spaces = 2 * (n - i - 1)
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)