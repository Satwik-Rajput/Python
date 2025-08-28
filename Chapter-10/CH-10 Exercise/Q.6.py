# NOthing will happen.For example i use ud instead of self but nothing will happen.
from random import randint
class train:

    def __init__(ud,trainNO):
        ud.trainNo = trainNO

    def book(ud,fro,to):
        print(f"Train No: {ud.trainNo} has been booked from {fro} to {to}")

    def tainstatus(ud):
        print(f"Train No: {ud.trainNo} is running on time")

    def bookingfair(ud,fro,to):
        print(f"Train No: {ud.trainNo} has been booked from {fro} to {to} for {randint(1000,2000)} rupees")

t = train(2089)
t.book("Agra","Delhi")
t.tainstatus()
t.bookingfair("Agra","Delhi")