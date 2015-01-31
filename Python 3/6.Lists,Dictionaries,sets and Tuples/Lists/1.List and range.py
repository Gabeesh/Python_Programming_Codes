'''

? List constants are surrounded by
square brackets and the elements in
the list are separated by commas
? A list element can be any Python
object - even another list
? A list can be empty

? Strings are ?immutable? - we
cannot change the contents of a
string - we must make a new
string to make any change
? Lists are ?mutable? - we can
change an element of a list
using the index operator

'''

list = [ 1, [5, 6], 7]

print list

print len(list)

dir(list)

'''

? The range function returns a list
of numbers that range from zero
to one less than the parameter
? We can construct an index loop
using for and an integer iterator

'''

print range(4)


a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print c

dir(c)

#d = list()

#dir(d)


