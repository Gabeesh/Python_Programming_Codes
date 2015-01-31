akhil = open('UserDetails.txt')
for line in akhil:
    line = line.rstrip()
    if not 'student' in line :
        continue
    print line

'''
? We can look for a string
anywhere in a line as our
selection criteria

'''
fhand = open('mbox-short.txt')
for lin in fhand:
    lin= lin.rstrip()
    if not '@uct.ac.za' in lin :
        continue
    print lin