# Create a clas (2D vector) and use it create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                  # str() is used to represent the object in a readable format
        return f"{self.x}i + {self.y}j"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

v2 = Vector2D(1, 2)
v3 = Vector3D(1, 2, 3)
print(v2)
print(v3)