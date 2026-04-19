# Object Oriented Programming (OOP)
# OOP is a programming paradigm that uses "objects" to design applications. 
# Objects are instances of classes, and they contain data (attributes) and methods (functions) that operate on that data.

# Class: A blueprint for creating objects. It defines the attributes and methods that all objects of that class will have.
# Object: An instance of a class. It has its own set of data and can perform the actions defined by its class.

# Attributes: Variables that store data about an object.
# Methods: Functions that define the behavior of an object.

# Example:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Create objects of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Access attributes and methods
print(dog1.name)
print(dog2.age)
dog1.bark()
dog2.bark() 