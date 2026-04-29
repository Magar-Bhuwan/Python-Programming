# Format method is used to format strings by replacing placeholders with actual values.
# The syntax for the format method is: "string with placeholders".format(values)

# Example 01:
name = "Ramlal"
age = 27
result = "My name is {} and I am {} years old.".format(name, age)
print (result)

# Example 02:
# f string is a more concise way to format strings, introduced in Python 3.6
result2 = f"My name is {name} and I am {age} years old."
print(result2)

# Example 03:
# You can also specify the order of the placeholders using numbers
result3 = "My name is {0} and I am {1} years old. {0} is a good name.".format(name, age)
print(result3)
