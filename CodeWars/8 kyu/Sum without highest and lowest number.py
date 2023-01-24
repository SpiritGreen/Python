'''
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
'''

def sum_array(arr):
  if (not arr or len(arr) < 1):
    return 0
  arr.sort()
  arr = arr[1:-1]
  return sum(arr)

print(sum_array())