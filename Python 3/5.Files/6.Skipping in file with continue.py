fhand = open('UserDetails.txt')
for line in fhand:
    line = line.rstrip()
    if  line.startswith('1') : # 'or' if not line.startswith('1') :
        continue
    print line

'''

? We can conveniently
skip a line by using the
continue statement
'''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') : # Pls remind "if not"
        continue
    print line