#Write a program to make a copy of text file "this.txt"

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\this.txt", "r") as f:
    content = f.read()
    with open(r"D:\ML with Python\Python\Chapter 9 - File IO\this_copy.txt", "w") as f:
        f.write(content)
