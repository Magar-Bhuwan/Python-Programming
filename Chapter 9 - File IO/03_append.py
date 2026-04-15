str_line = input("Enter your message: ")

f = open(r"D:\ML with Python\Python\Chapter 9 - File IO\myfile2.txt", "a")

f.write(str_line)

f.close()