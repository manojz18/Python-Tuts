
class Employee:
    name = "John"
    lang = "python"

    def printing(self):
        print("Inside the class Fuction")

    def getInfo(self):
        print(f"name is {self.name} and lang is {self.lang}")

    @staticmethod #by using staticmethod we donot require self attribute
    def greet():
        print("Welcome to Goa Singham")

    


j = Employee()

j.lang = "C++"
print(j.name, j.lang)

# j.getInfo() => this gives error bcoz it is converted to -> j.getinfo(j) so we need to write "self" in the function parameter 
j.printing()

j.getInfo()
j.greet()