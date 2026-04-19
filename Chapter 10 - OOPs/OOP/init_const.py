# __init__() is a special method in Python classes that is automatically called when an object of the class is created.
# It is used to initialize the attributes of the object.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.name)
print(dog2.age) 