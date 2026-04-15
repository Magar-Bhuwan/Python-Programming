f = open(r"D:\ML with Python\Python\Chapter 9 - File IO\file1.txt")             #open(..) --> is a built in function use to open file and r".." --> ensures the path is treated as raw string 
data = f.read()                         #read() --> read the entire content of file and assign into 'data'/moves the cursor(pointer) from start to end
print(data)                             #print the entire file of data and show the content of file 
f.close()                               #close the file and frees system resources. now we cannot use f anymore

