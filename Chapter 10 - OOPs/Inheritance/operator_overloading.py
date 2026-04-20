# Operator Overloading
# Operator overloading is a feature that allows you to define the behavior of operators for user-defined types
# syntax: operator.operator_name

# Example 1:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self, other):
        return self.age + other.age

student1 = Student("John", 20)
student2 = Student("Jane", 25)

print(student1 + student2)

# Example 2:

class Numbers:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return self.num + other.num

    def __str__(self):
        return f"The number is {self.num}"

num1 = Numbers(10)
num2 = Numbers(20)

print(type(num1))
print(type(num2))
print(type(num1 + num2))

result = num1 + num2
print(result)


# there are other operators that can be overloaded
# n1.__sub__(n2) for subtraction
# n1.__mul__(n2) for multiplication
# n1.__truediv__(n2) for division
# n1.__floordiv__(n2) for floor division
# n1.__mod__(n2) for modulo
# n1.__pow__(n2) for power
# n1.__eq__(n2) for equality
# n1.__ne__(n2) for inequality
# n1.__lt__(n2) for less than
# n1.__le__(n2) for less than or equal to
# n1.__gt__(n2) for greater than
# n1.__ge__(n2) for greater than or equal to

