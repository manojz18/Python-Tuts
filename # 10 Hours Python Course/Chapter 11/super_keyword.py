class Coder:
    language = "C++"

    def __init__(self):
        print("Coder Constructor")

    # def printLang(self):
    #     print(f"The language of coder is: {self.language}")

class Programmer(Coder):
    lang = "Java"

    def __init__(self):
        super().__init__()
        print("Programmer Constructor")

    # def myLang(self):
    #     print(f"The language of Programmer is: {self.lang}")

class NoCoding(Programmer):
    languages = "Marathi"

    
    def __init__(self):
        super().__init__()  
        print("NoCoding Constructor")
        # super().__init__()

    # def mTongue(self):
    #     print(f"The language of NoCoding is: {self.languages}")


obj = NoCoding()
