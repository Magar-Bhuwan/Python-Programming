'''
=> loops are use to repeate the same block of code in multiple times based on a 
condition or over a sequence of items with automatically.
=> loops make programs shorter and easier to read.
=> loops can be nested loops
=> loop control statements (break, continue, else with loops)

There are 2 types of loops in Python
1. for loop
2. while loop

'''
# example: we have to print 1 - 100 numbers

# we can use print in 100 times

print(1)
print(2)
print(3)
print(4)
print(5)
print("...")
print(100)

#Or we have better option using for loop

for i in range(1,101):              #Indexing rage(1,101)
    print(i)
