__author__ = 'AKHIL REDDY'

class Enemy:

    def __init__(self,x):
        self.energy = x

    def get_energy(self):
        print(self.energy)    # We are able to access energy as it is self.energy variable.
                              # We can access varibles in __init__ function when ever needed locally.


lilly = Enemy(5)
akki = Enemy(20)

lilly.get_energy()
akki.get_energy()



