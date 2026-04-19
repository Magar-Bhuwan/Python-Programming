# Write a class Train which have methods to book a ticket, get status(no of seats) and get fare information 
# of train running under Indian Railway.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The train {self.name} has {self.seats} seats left.")

    def getFare(self):
        print(f"The fare of train {self.name} is {self.fare}.")

    def bookTicket(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"Ticket booked for train {self.name}.")
        else:
            print(f"No seats left in train {self.name}.")

t1 = Train("Rajdhani Express", 1000, 5)
t1.getStatus()
t1.getFare()
t1.bookTicket()
t1.getStatus()