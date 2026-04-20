# Multiple inheritance is a mechanism in which a class acquires the properties of multiple parent classes.

# syntax:
# class child_class(parent_class1, parent_class2, ...):
#     # body of child class

class Father:
    def __init__(self, name):
        self.name = name
    
    def father_name(self):
        print(f'Father name = {self.name}')

class Mother:
    def __init__(self, name):
        self.name = name

    def mother_name(self):
        print(f'Mother name = {self.name}')

#child class which is multiple inheritance
class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)              #calling parent class constructor
        Mother.__init__(self, mother_name)              #calling parent class constructor
        self.child_name = child_name

    def show_child_name(self):
        print(f'Child name = {self.child_name}')

f_name = input("Enter your Father Name: ")
m_name = input("Enter your Mother Name: ")
c_name = input("Enter your Child Name: ")
print("\n")

child1 = Child(f_name, m_name, c_name)

child1.father_name()
child1.mother_name()
child1.show_child_name()
