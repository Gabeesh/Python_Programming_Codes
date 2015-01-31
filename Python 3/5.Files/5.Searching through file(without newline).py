fhand = open('UserDetails.txt')
for line in fhand:
    line = line.rstrip() #Used to leave newline in text file
    if line.startswith('1'):
        print line

'''
? Each line from the file has a
newline at the end
? The print statement adds a
newline to each line

? We can strip the whitespace
from the right-hand side of the
string using rstrip() from the
string library
? The newline is considered
?white space? and is stripped

'''