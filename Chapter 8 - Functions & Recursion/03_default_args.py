def Hello(name, end = "Thank You!"):                    #name is a user arguments and end is a default arguments
    print(f'My name is {name}')
    print(end)

Hello("Ramlal")                                         # we are given name but not end arguments so it put default end arguments "Thank You!"
Hello("Ramlal", "Thanks! ")                             #given both name and end arguments so it put name + "Thanks!"