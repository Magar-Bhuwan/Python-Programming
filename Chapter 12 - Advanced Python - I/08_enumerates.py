# Enumerates function is used to iterate over an iterable and get the index of each item


# we can deal with this type of iteration process using for loop.
# and it will be more cumbersome for us to maintain the code. and it will be more error-prone.
l = [3, 6, 9, 123, 576, 890]

index = 0
for item in l:
    print(f"The item number {index} is {item}")
    index += 1
print("\n")

# So, we can use enumerate function to iterate over an iterable and get the index of each item.
# and it will be more efficient and less error-prone.

l = [3, 6, 9, 123, 576, 890]

for index, item in enumerate (l):
    print(f"The item number {index} is {item}")
