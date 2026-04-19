# Write a program to find out whether a given post is talking about "Harry" or not?

post = input("Enter the post: ")

if("Harry".lower() in post.lower()):                        #.lower() => convert the lower case and checks
    print("This post is talking about Harry. ")

else:
    print("This post is not talking about Harry. ")
