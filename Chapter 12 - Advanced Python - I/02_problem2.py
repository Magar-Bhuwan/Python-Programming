# Write a to print third, fifth and seventh element from a list using enumerates function

l = [2, 5, 6, 12, 68, 24, 78, 845, 322, 235]

for index, l in enumerate (l):
    if index == 2 or index == 4 or index == 6:
        print(f"Index number {index} value is {l}")