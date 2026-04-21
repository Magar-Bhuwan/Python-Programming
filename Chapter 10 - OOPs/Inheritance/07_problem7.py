# Write a __str__ method to print the vector as follows
# 7i + 8j + 10k
# Assumes vector of dimensions3 for this problem.

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
        return f'Vector =  {self.x}i + {self.y}j + {self.z}k'

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)