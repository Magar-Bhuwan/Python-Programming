# if languages of two friends are same; what will happen to program in problem 6?
s = {}

name = input ("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})

name = input ("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})

name = input ("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})

name = input ("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name: lang})

print(s)
print("Nothing will happen (values can be same) it prints same languages for different person. ")