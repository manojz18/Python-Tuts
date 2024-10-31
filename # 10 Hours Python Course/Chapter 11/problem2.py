
class Animals:
    animal = "Dog"

class Pets(Animals):
    pet = "Pet Dog"

class Dog(Pets):
    def bark(self):
        print("This is Germansheferd and it barks")


d = Dog()
d.bark()