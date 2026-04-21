# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' for the 'Pets' class. 
# Add a method 'bark' to the class 'Dog'

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("The Dog Bark like: Bow! Bow! Bow!")

dog1 = Dog()

dog1.bark()



# class Animals:
#     def __init__(self, name):
#         self.name = name

# class Pets(Animals):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

# class Dog(Pets):
#     def __init__(self, name, color):
#         super().__init__(name, color)

#     def bark(self):
#         print(f"{self.name} have {self.color} color is bark. ")

# dog1 = Dog("Tommy", "Brown" )
# dog2 = Dog("Jacky", "Black" )

# print(dog1.name)
# print(dog1.color)
# dog1.bark()




