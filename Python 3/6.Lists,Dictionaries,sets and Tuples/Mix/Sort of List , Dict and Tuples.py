'''
? We can take advantage of the ability to sort a list of tuples to
get a sorted version of a dictionary
? First we sort the dictionary by the key using the items()
method

'''
d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t
t.sort()
print t

'''
 We can do this even
more directly using the
built-in function sorted
that takes a sequence as a
parameter and returns a
sorted sequence
'''
d = {'a':10, 'b':1, 'c':22}
print d.items()
t = sorted(d.items())
print t
for k, v in sorted(d.items()):
    print k, v
'''
Sort by values instead of key:

? If we could construct
a list of tuples of the
form (value, key) we
could sort by value
? We do this with a for
loop that creates a list
of tuples

'''

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
print tmp
tmp.sort()
print tmp
tmp.sort(reverse = True) # Argument used to sort in reverse order
print tmp