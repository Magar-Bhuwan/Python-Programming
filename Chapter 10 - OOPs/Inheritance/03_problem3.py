# Create a class 'Employee' and add salary and increment properties to it.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showdetails(self):
        print(f"Employee name: {self.name}")
        print(f"Employee initial Salary: {self.salary}")

class Increment_Salary(Employee):
    def __init__(self, name, salary, add_sal):
        super().__init__(name, salary)
        self.add_sal = add_sal

    def final_salary(self):
        sal = self.salary + self.add_sal
        print(f"{self.name} have previouse salary: {self.salary} and After Incrememtn salary: {sal}")

emp1 = Increment_Salary("Ramlal", 50000, 4500)
emp2 = Increment_Salary("Sita Kumari", 60000, 4500)

emp1.showdetails()
emp2.showdetails()

emp1.final_salary()
emp2.final_salary()