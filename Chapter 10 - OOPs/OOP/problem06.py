# Can you change the self-parameter inside a class to something else (say "ram"). 
# Try changing self to "slf" or "ram" and see the effects.

class Train:
    def __init__(slf, name, fare, seats):               # self is just a convention, we can use any other name for the first parameter of a class.
        slf.name = name
        slf.fare = fare
        slf.seats = seats

    def getStatus(ram):
        print(f"The train {ram.name} has {ram.seats} seats left.")

    def getFare(ram):
        print(f"The fare of train {ram.name} is {ram.fare}.")

    def bookTicket(slf):
        if slf.seats > 0:
            slf.seats -= 1
            print(f"Ticket booked for train {slf.name}.")
        else:
            print(f"No seats left in train {slf.name}.")

t1 = Train("Rajdhani Express", 1000, 5)
t1.getStatus()
t1.getFare()
t1.bookTicket()
t1.getStatus()


# Instead of use of self we can use any other name for the first parameter of a class. like we used slf and ram.