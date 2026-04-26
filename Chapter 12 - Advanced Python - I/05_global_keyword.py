# Global Varible / Keyword

def fun():
    global a        # if we change global a then it will make local variable also global variable
    a = 56          #local variable for fun() function
    print(a)

a = 12              # Global variable for all

fun()
print(a)