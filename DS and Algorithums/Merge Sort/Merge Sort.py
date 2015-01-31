#-------------------------------------------------------------------------------
#
# Author:      AKHIL REDDY
#
#-------------------------------------------------------------------------------
'''
Here I am using Merge Sort with Timecomplexity of O(nlogn) to sort is best possible
Short time for Million Integers.
'''
def main():
    pass

def sort( List ):
      List = mergesort( List, 0, len( List ) - 1 )
      return List

def mergesort( List, first, last ):
  mid = ( first + last ) / 2
  if first < last:
    mergesort( List, first, mid )
    mergesort( List, mid + 1, last )

  a, f, l = 0, first, mid + 1
  temp = [None] * ( last - first + 1 )

  while f <= mid and l <= last:
    if List[f] < List[l] :
      temp[a] = List[f]
      f += 1
    else:
      temp[a] = List[l]
      l += 1
    a += 1

  if f <= mid :
    temp[a:] = List[f:mid + 1]

  if l <= last:
    temp[a:] = List[l:last + 1]

  a = 0
  while first <= last:
    List[first] = temp[a]
    first += 1
    a += 1
  return List

if __name__ == '__main__':
    main()

List = range(1,100000) # Here I am Taking a Tuple with values ranging from 1 to 1000000 but we can take it in any order to Sort.
print sort(List)