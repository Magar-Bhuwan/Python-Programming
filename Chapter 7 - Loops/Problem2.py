# Write a program to greet all the person names stored in a list "l" and which starts with S.

l = ["Harry", "Subham", "Yaman", "Sundar", "Rohan"]

for name in l:
    if(name.startswith("S")):           #.startswith method checks the String starting with "S", and false otherwise
        print(f"Hello {name}")          #f-string, which allows us to insert the value of name directly in the string.
        
