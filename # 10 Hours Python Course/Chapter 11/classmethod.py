
class Service:
    a = 10

    @classmethod
    def show(cls):
        print(f"Show value of class attr a: {cls.a}")


obj = Service()
obj.a = 15
obj.show()