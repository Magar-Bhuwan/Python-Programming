f = open(r"D:\ML with Python\Python\Chapter 9 - File IO\myfile1.txt", 'r')      #we dont neet to write 'r' mode it is in default read mode 
print(f.read())
f.close()

# The same can be written using with statement like this:
with open(r"D:\ML with Python\Python\Chapter 9 - File IO\myfile1.txt", 'r') as f:
    print(f.read())

#You don't have to explicitly close the file. 