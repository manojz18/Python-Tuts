class Vector:
    def __init__(self, list):
        self.list = list

    
    def __len__(self):
        return len(self.list)
    

c1 = Vector([1, 2, 3])
# c2 = Vector(4, 5, 6)
print(len(c1))