class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, c2):
        result = Vector(self.i + c2.i, self.j + c2.j, self.k + c2.k)
        return result
    
    def __mul__(self, c2):
        result = self.i * c2.i + self.j * c2.j + self.k * c2.k
        return result

    def __str__(self):
        return f"({self.i}i + {self.j}j + {self.k}k)"
    

c1 = Vector(1, 2, 3)
c2 = Vector(4, 5, 6)

print(c1+c2)
print(c1*c2)