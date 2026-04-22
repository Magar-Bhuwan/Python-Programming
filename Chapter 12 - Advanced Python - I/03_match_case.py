# match case
# match case is introduced in Python 3.10.
# It is a modern alternative to if-elif-else ladder called structural pattern matching.

# syntax:
# match variable:
#     case pattern1:
#         # code
#     case pattern2:
#         # code
#     case _:
#         # default case

# Example 1:

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(418))

# Example 2: Match Strings

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")

# Example 3: Multiple values in one case

num = 2

match num:
    case 1 | 2 | 3:
        print("Small number")
    case _:
        print("Other number")

# Example 4: Matching Lists

data = [1, 2]

match data:
    case [a, b]:
        print(f"Two elements: {a}, {b}")
    case _:
        print("Something else")

# Example 5: Matching Dictionaries

person = {"name": "John", "age": 30}

match person:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
    case _:
        print("Something else")

# Example 6: Matching Tuples

point = (1, 2)

match point:
    case (x, y):
        print(f"x: {x}, y: {y}")
    case _:
        print("Something else")

# Example 7: Matching Classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)

match point:
    case Point(x, y):
        print(f"x: {x}, y: {y}")
    case _:
        print("Something else")
