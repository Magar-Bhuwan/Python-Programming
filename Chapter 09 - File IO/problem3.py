#Write a program to generate the multiplication tables from 2 to 20 and write it to the different files.
#Place these files in a folder for a 13 years old.

def generate_table(n):
    tables = ""
    for i in range(1, 11):
        tables += f"{n} x {i} = {n*i}\n"
    with open(f"D:\\ML with Python\\Python\\Chapter 9 - File IO\\Tablesm\\Table of {n}.txt", "w") as f:
        f.write(tables)  
    print(f"Table of {n} generated successfully!")
       
for i in range(2, 21):
    generate_table(i)

