from random import randint
class train:

    def __init__(self,trainNO):
        self.trainNo = trainNO

    def book(self,fro,to):
        print(f"Train No: {self.trainNo} has been booked from {fro} to {to}")

    def tainstatus(self):
        print(f"Train No: {self.trainNo} is running on time")

    def bookingfair(self,fro,to):
        print(f"Train No: {self.trainNo} has been booked from {fro} to {to} for {randint(1000,2000)} rupees")

t = train(2089)
t.book("Agra","Delhi")
t.tainstatus()
t.bookingfair("Agra","Delhi")