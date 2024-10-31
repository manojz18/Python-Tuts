from random import randint

class Train:
    def book(self, trainNo, fromm, to):
        print(f"The ticket is booked for the train {trainNo} from {fromm} to {to}")

    def getStatus(self, trainNo):
        print(f"The train {trainNo} is Running on time")

    def getFare(self, trainNo, fromm, to):
        print(f"The fare of train {trainNo} from {fromm} to {to} is {randint(500, 1001)}")


t = Train()
t.book("15209", "Pune", "Daund")
t.getStatus("15209")
t.getFare("15209", "Pune", "Daund")