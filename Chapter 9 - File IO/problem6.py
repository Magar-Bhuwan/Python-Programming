#Write a program to mine a log file and find out the wether it contains "python"

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\log.txt", "r") as f:
    content = f.read()
    if "python" in content:
        print("Python is presetn in the log file")
    else:
        print("Python is not presetn in the log file")

    