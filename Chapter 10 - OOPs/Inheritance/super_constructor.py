# super() constructor
# super() is used to call the constructor of the parent class
# syntax: super().__init__()

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def eat(self):
        print(f'{self.name} is eating. ')

class Dog(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name, color)       # calling parent class constructor
        self.breed = breed

    def bark(self):
        print(f'{self.name} is barking. ')

dog1 = Dog('Jacky', 'Black', "German Shepherd")

print(f"Name of Dog = {dog1.name}")
print(f"Color of Dog = {dog1.color}")
print(f"Breed of Dog = {dog1.breed}")
dog1.eat()
dog1.bark()

print(Dog.__mro__)                  # Method Resolution Order
print(Dog.__doc__)                  # Docstring
print(Dog.__name__)                 # Class name
print(Dog.__module__)               # Module name
print(Dog.__bases__)                # Parent classes
print(Dog.__dict__)                 # Class attributes