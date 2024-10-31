class Coder:
    language = "C++"
    def printLang(self):
        print(f"The language of coder is: {self.language}")

class Programmer(Coder):
    lang = "Java"
    def myLang(self):
        print(f"The language of Programmer is: {self.lang}")


ob = Programmer()
ob.myLang()
ob.printLang()