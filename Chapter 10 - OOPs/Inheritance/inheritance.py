# inheritance is a mechanism in which one class acquires the properties of another class.
# the class which acquires the properties of another class is called child class or derived class.
# the class whose properties are acquired is called parent class or base class.

# syntax:
# class child_class(parent_class):
#     # body of child class

# parent class
class Animal:                   
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating. ")

# child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking. ")

#creating class object
dog = Dog("Buddy")

#calling parent class method
dog.eat()

#calling child class method
dog.bark()
