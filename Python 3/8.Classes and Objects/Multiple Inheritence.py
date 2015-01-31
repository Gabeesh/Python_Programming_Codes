__author__ = 'AKHIL REDDY'
class Mario():

    def move(self):
        print("I am moving")

class Shroom():

    def eat_shroom(self):
        print("Now I'm Big")

class Big_Mario(Mario,Shroom):
    pass                           # Pass is use to allow new class of multiple inheritence without any its own functions ( solves traceback )

akki = Big_Mario()

akki.move()
akki.eat_shroom()


