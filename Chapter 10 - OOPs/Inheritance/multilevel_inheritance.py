# Multilevel inheritance is a mechanism in which a class acquires the properties of multiple parent classes.

# syntax:
# class parent_class:
#     # body of parent class

# class child_class(parent_class):
#     # body of child class

# class grandchild_class(child_class):
#     # body of grandchild class

# Example of multilevel inheritance
# parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")

# child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# grandchild class
class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing.")

# creating class object
puppy = Puppy("Buddy")

# calling parent class method
puppy.eat()

# calling child class method
puppy.bark()

# calling grandchild class method
puppy.play()
