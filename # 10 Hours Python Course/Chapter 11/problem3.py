class Employee:
    salary = 200000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSalary):
        self.increment = ((newSalary/self.salary)-1)*100

e = Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 500000
print(e.increment)