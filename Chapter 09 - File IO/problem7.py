#Write a program to find out the line number where python is present from question 6

# Find line numbers where "python" is present in the file

with open(r"D:\ML with Python\Python\Chapter 9 - File IO\log.txt", "r") as f:
    lines = f.readlines()
    found = False

    for lineno, line in enumerate(lines, start=1):  # enumerate handles line counting
        if "python" in line.lower() or line.capitalize():                # .lower() for case-insensitive match
            print(f"'python' is present at line no: {lineno}")
            found = True

    if not found:
        print("'python' is not present in the log file")
