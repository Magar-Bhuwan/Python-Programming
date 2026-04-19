# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = 0.
# Does this change the class attribute?

class Demo:
    a = 10

obj = Demo()

print(obj.a)            # it prints class attribute

obj.a = 0               # it creates instance attribute
print(obj.a)            # it prints instance attribute

print(Demo.a)           # it prints class attribute 

# So, it does not change the class attribute.
