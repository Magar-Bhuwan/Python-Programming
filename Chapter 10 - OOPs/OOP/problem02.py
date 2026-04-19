# Write a program with class "Calculator" capable of finding square, cube, square root, cube root of a number.

class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num

    def squareRoot(self):
        return self.num ** 0.5

    def cubeRoot(self):
        return self.num ** (1/3)

calc = Calculator(9)

print("Square of 9 is: ", calc.square())
print("Cube of 9 is: ", calc.cube())
print("Square root of 9 is: ", calc.squareRoot())
print("Cube root of 9 is: ", calc.cubeRoot())