'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
'''

def count_positives_sum_negatives(arr):
  positive_count = 0
  negative_sum = 0
  for num in arr:
    if num > 0:
      positive_count += 1
    elif num < 0:
      negative_sum += num
  if len(arr) == 0:
    return []
  else:
    return [positive_count, negative_sum]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))