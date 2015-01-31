__author__ = 'AKHIL REDDY'

class Enemy:
    life = 3

    def attack(self): # self is const arg. which specifies that function is itself from class
        print("Vammo Sacchanu ra babaoye!!!")
        self.life -= 1
        self.ok='Hurray'

    def checklife(self):
        if self.life <= 0:
            print ("Hurray!I am Dead")
        else:
            print(str(self.life) + " Life is Left")
        print self.ok # we are able to access even variables in another function by using "self" .



enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy2.attack()

enemy1.checklife()
enemy2.checklife()

