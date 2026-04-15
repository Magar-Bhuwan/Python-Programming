#Write a program to remove a given word from a list ad strip it at the same time.

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))              #strip(word) --> doenot remove the word from the middle
                                                    #it removes characters of word from the begining and end only
    return n

l = ["Pujan", "Rohan", "Ram", "Pritam", "an"]
print(rem(l, "an"))