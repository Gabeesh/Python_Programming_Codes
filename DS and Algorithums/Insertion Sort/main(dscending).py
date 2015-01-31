__author__ = 'AKHIL REDDY'

array = list()

#count=int(input("Pls give total number for the list:"))
count=int(input())

#print(count)

i=1
while i<=count:
  #  print("Pls give",i," number of the list:")
    inp = input()
    array.append(int(inp))
    i=i+1

j=1
while j<count:
    key = array[j]
    i = j-1
    while i>=0 and array[i]<key :
        array[i+1]=array[i]
        i = i-1
    array[i+1]=key
    j=j+1

i=0
while i< count:
    print(array[i])
    i = i+1






