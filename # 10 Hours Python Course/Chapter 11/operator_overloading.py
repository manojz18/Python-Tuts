class Number:

    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
obj1 = Number(5)
obj2 = Number(10)

print(obj1+obj2)

