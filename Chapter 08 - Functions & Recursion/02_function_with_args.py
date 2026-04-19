def intro(name, age):                       #defining function with arguments or parameters
    # print("Hello my name is " + name)
    # print("My age is " + str(age))          #Converting integer to string
    print(f"Hello my name is {name}")
    print(f"My age is {age}") 
    return "Thank You! "                      #return value      

a = intro("Ramlal", 25)
a = intro("Prakriti", 22)
a = intro("Hari", 29)
a = intro("Nirmal", 40)

print(a)                                       #print return value
