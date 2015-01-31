'''
? We can put an if statement in
our for loop to only print lines
that meet some criteria

'''


fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print line