__author__ = 'AKHIL REDDY'

class Girl:

    gender = 'female'

    def __init__(self,name):
        self.name = name      # varable initalised or added with self can be acessed any way in class (i.e its functions)

snikky = Girl('akshitha')
gunny = Girl('pranamika')

print(snikky.gender)
print(snikky.name)

print(gunny.name)
print(gunny.gender)

