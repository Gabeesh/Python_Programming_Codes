__author__ = 'AKHIL REDDY'

import threading

class Akki_Messenger(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = Akki_Messenger(name = 'I am Sending Messages')
y = Akki_Messenger(name= 'I am Recieving Messages')

# x.run()
# y.run()

x.start()
y.start()

