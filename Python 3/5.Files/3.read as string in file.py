'''
Reading the *Whole* File
? We can read the whole file
(newlines and all) into a
single string by using read() function

'''


fhand = open('UserDetails.txt')
inp = fhand.read()
print len(inp)

print inp[:2]
print inp[2:14]