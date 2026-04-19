# String Slicing

# First Method
name = "Ramlal"
nameshort = name[0:3]   #Start from index 0 to till 3 but not include 3
print(nameshort)

charcter1 = name[3]
print(charcter1)

# Second Method

name1 = "Santosh"
print(name1[-4:])
print(name1[-4:-1])
print(name1[-4:-2])

# Slicing with skip value
w = "1234567890"
print(w[1:7])
print(w[1:7:3])     #Where 3 is skipping value

