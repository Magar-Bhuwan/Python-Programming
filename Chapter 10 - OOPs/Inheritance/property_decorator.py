#property decorator
# syntax: @property
# it is used to create a property
# it is used to create a getter, setter, and deleter
# it is used to create a property that is not a method

# Example 1:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
    
    @age.deleter
    def age(self):
        print("Age is deleted!")
        del self._age

student1 = Student("John", 20)
print(student1.age)

student1.age = 25
print(student1.age)

del student1.age

if hasattr(student1, 'age'):
    print(student1.age)
else:
    print("Age no longer exists!")