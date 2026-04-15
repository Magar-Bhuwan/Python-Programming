str = "Hello! How are you?"

f = open(r"D:\ML with Python\Python\Chapter 9 - File IO\myfile1.txt", "r+")     #use "w" --> for write/ "r+" --> for read and write

f.write(str)

f.read()
print(str)

f.close