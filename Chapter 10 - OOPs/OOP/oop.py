# Object Oriented Programming (OOP)
# OOP is a programming paradigm that uses "objects" to design applications. 
# Objects are instances of classes, and they contain data (attributes) and methods (functions) that operate on that data.

# Class: A blueprint for creating objects. It defines the attributes and methods that all objects of that class will have.
# Object: An instance of a class. It has its own set of data and can perform the actions defined by its class.

# Attributes: Variables that store data about an object.
# Methods: Functions that define the behavior of an object.

# Example:
class Dog:
    def __init__(self, name, age):             # constructor
        self.name = name                
        self.age = age                  

    def bark(self):                             # Self is a reference to the current instance of the class
        print(f"{self.name} says Woof!")

    @staticmethod                               # @staticmethod is use for creating a method that is not dependent on any instance of the class
    def sit():                                  # don't need to pass self as an argument
        print(f"The dog is sitting.")

# Create objects of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)
dog1.name = "Jacky"                       # instance attribute which is more priority than class attribute

# Access attributes and methods

print(dog1.name)
print(dog2.age)
dog1.bark()
dog2.bark() 
dog1.sit()
