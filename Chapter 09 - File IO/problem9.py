#Write a program to find out whether a file is identical & matches the content of another file

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\this.txt", "r") as f:
    content1 = f.read()

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\this_copy.txt", "r") as f:
    content2 = f.read()
if content1 == content2:
    print("The file contents are identical. ")
else:
    print("The file contents are not identical. ")

