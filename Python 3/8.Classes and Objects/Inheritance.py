__author__ = 'AKHIL REDDY'

class Parent():

    def print_last_name(self):
        print('Reddy')

class Child(Parent):

    def print_first_name(self):
        print('Akhil')

    def print_last_name(self): # If same One in Child is given Priority
        print('Marla')

akki = Child()

akki.print_first_name()
akki.print_last_name() # One function in same class is given priority over inherited one.


