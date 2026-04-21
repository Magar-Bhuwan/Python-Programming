# Write a class vector representing a vector of n dimensions. Overload the + and * operator
# which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, n1):
        result = Vector(self.x + n1.x, self.y + n1.y, self.z + n1.z)
        return result
    
    def __mul__(self, n1):
        result = self.x * n1.x + self.y * n1.y + self.z * n1.z
        return result
    
    def __str__(self):
        return f'Vecot ({self.x}, {self.y}, {self.z})'

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)