# Create a class "Programmer" for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self, name, age, salary, experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.company = "Microsoft"
        self.experience = experience

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")
        print(f"Experience: {self.experience}")

prgm1 = Programmer("Ram", 29, 50000, 2)
prgm2 = Programmer("Sham", 30, 60000, 3)
prgm3 = Programmer("Sita", 28, 70000, 4)
prgm4 = Programmer("Gita", 27, 80000, 5)

prgm1.details()
prgm2.details()
prgm3.details()
prgm4.details()   