# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "Buy now", "Subscribe this", "Click this".
# Write a program to detect these spams.

p1 = "make a lot of money" 
p2 = "buy now" 
p3 = "subscribe this" 
p4 = "click this"

message = input("Enter your comment. ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("The comment is spam. ")

else:
    print("The comment is not spam. ")

