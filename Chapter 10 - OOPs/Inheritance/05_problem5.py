# Write a class 'Complex' to represent complex numbers, along 
# with overload operators '+' and '*' which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, num2):
        return Complex(self.r + num2.r, self.i + num2.i)
    
    def __mul__(self, other):
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
        return Complex(real, imag)
    
    def __str__(self):
        return f'{self.r} + {self.i}i'


num1 = Complex(1, 2)
num2 = Complex(4, 3)

print(num1 + num2)  
print(num1 * num2) 