#Write a program to print following pattern
'''

****
***
**
* 

'''

def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)

pattern(5)