abc = 'With three words'
stuff = abc.split()
print stuff
['With', 'three', 'words']
print len(stuff)
print stuff[0]

'''
Split breaks a string into parts and produces a list of strings.  We think of these
as words.  We can access a particular word or loop through all the words.
'''

'''
? When you do not specify a delimiter, multiple spaces are treated like one delimiter
? You can specify what delimiter character to use in the splitting
'''


line = 'A lot               of spaces'
etc = line.split()
print etc
line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
thing = line.split(';')
print thing
print len(thing)