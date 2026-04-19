#Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'Twinkle'

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\poems.txt", 'r') as f:
    content = f.read()
    if("Twinkle" in content):
        print("The word Twinkle is presents in the file. ")
    else:
        print("The word Twinkle is not presents in the file. ")
