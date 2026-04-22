# type definitions in python
# type definitions usally refers how you define, specify, annotate data types in your code
# type definitions annotations helps in making the code self-documenting and easier to debug

# Example 1:

# Without type definitions
def add(a, b):
    return a + b

print(add(1, 2))

# With type definitions
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))


# 1. Built in data types:
x = 10        # int
y = 3.14      # float
name = "Ram"  # str
is_ok = True  # bool
lst = [1,2,3] # list


# 2. Type Checking:
print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_ok)) # <class 'bool'>
print(type(lst))   # <class 'list'>


# 3. Type Casting (Explicit Type Definition)
x = int("10")     # string → int
y = float(5)      # int → float
z = str(100)      # int → string


# 4. Type Hints (Static Type Definition)
def add(a: int, b: int) -> int:
    return a + b


# 5. Using Typing Module
from typing import List, Dict, Tuple, Optional

# List
numbers: List[int] = [1, 2, 3]

# Dictionary
person: Dict[str, int] = {"age": 30, "height": 170}

# Tuple
coordinates: Tuple[int, int] = (10, 20)

# Optional
age: Optional[int] = None


# 6. Type Aliases
from typing import List

Scores = List[int]
marks: Scores = [80, 90, 70]


# 7. Custom Type Hints
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def greet(student: Student) -> str:
    return f"Hello, {student.name}!"


# 8. Union Types (Multiple Possible Types)
from typing import Union

def display(value: Union[int, str]):
    print(value)
    
#👉 Python 3.10+ shortcut:
def display(value: int | str):
    print(value)






