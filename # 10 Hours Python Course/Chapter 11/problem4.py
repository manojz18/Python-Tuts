class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return f"{self.r + c2.r} + {self.i + c2.i}i"
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        img_part = self.r * c2.i + self.i * c2.r

        return f"{real_part} + {img_part}i"
    

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1+c2)
print(c1*c2)