# Multiples of 3 or 5
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
'''

def solution(number):
  if number < 0:
    return 0
  else:
    num_lst = [x for x in range(number)]
    result = 0
    for num in num_lst:
      if num%3 == 0:
        result += num
      elif num%5 == 0:
        result += num
  return result

print(solution(16))

'''
Оптимальное решение:
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
'''