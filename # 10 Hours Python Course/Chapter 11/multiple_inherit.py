class Coder:
    language = "C++"
    def printLang(self):
        print(f"The language of coder is: {self.language}")

class Programmer:
    lang = "Java"
    def myLang(self):
        print(f"The language of Programmer is: {self.lang}")

class NoCoding(Coder, Programmer):
    languages = "Marathi"
    def mTongue(self):
        print(f"The language of NoCoding is: {self.languages}")


obj = NoCoding()
obj.printLang()
obj.myLang()
obj.mTongue()