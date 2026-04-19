# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, num):
        self.num = num

    @staticmethod                       # static method
    def greet():
        print("Hello, Good Morning!")
    
    def square(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num

    def squareRoot(self):
        return self.num ** 0.5

    def cubeRoot(self):
        return self.num ** (1/3)

calc = Calculator(9)

calc.greet()          # calling static method   
print("Square of 9 is: ", calc.square())
print("Cube of 9 is: ", calc.cube())
print("Square root of 9 is: ", calc.squareRoot())
print("Cube root of 9 is: ", calc.cubeRoot())