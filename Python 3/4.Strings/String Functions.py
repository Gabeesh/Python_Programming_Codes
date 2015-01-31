great = 'Hellow AKHIL'

aki = great.lower()

print aki

aki = great.upper()

print 'Hi THere'.lower()

print dir(aki)

fruit = 'banana'
pos = fruit.find('na')
print pos

aa = fruit.find('z')
print aa

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print nstr
print greet
nstr = greet.replace('o','X')
print nstr

greet = '   Hello Bob  '
print greet.lstrip()
print greet.rstrip()
print greet.strip()

line = 'Please have a nice day'
if line.startswith('Please'):
    print "True"
if line.startswith('p'):
    print "False"
