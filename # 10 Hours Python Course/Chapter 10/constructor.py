class Create:
    #  def __init__(self):  #default constructor
    #     print("I am called dunder method, which donot require to be call(constructor)")

    def __init__(self, name, salary):
        print(f"Your name and salary is {name}, {salary}")

j = Create("Rohan", "120000")
