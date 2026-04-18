#Write a program to which contains a word "Donkey" multiple times. You need to replace this word with ###### by updating the same file

word = "Donkey"

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\donkey.txt", "r") as f:
    content = f.read()
    if word in content:
        content = content.replace(word, "######")
        print("Successfully replaced the word 'Donkey' with '######'")
    else:
        content = content.replace("######", word)
        print("Successfully replaced the word '######' with 'Donkey'")

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\donkey.txt", "w") as f:
    f.write(content)
