file = open('Sample.txt', 'w')

file.write('I am aKhil reddy marla\n')
file.write('I am an Indian')

file.close()

file = open('Sample.txt', 'r')
text = file.read()
print(text)

file.close()