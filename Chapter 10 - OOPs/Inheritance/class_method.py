# class method
# syntax: @classmethod
# class method is a method that is bound to the class and not to the instance
# it is called using the class name
# it takes the class as the first argument
# it is used to create class objects

# Example 1:

class Employee:
    a = 1
    def show(self):         # instance method shows the instance variable
        print(f" The class value of a is: {self.a}")

#or
    @classmethod            # class method shows the class variable
    def show(cls):          # class method shows the class variable
        print(f"{cls.a}")

e = Employee()
e. a = 40                   # instance variable

e.show()                    # instance method shows the instance variable
Employee.show()             # class method shows the class variable


# Example 2:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod                                    # class method
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("John", 20)
student1.show()

student2 = Student.from_birth_year("Jane", 2004)
student2.show()
