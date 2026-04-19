#Repeat program 4 for a list of such words to be censored. 

words = ["Donkey","animal"]

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\donkey.txt", "r") as f:
    content = f.read()
    for word in words:
        if word in content:
            content = content.replace(word, "######")
            print("Successfully replaced the word 'Donkey' with '######'")
    print(content)

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\donkey.txt", "w") as f:
    f.write(content)



