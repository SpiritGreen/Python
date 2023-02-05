'''
Реализуйте функцию is_power_of_three(), которая определяет, является ли переданное число натуральной степенью тройки. Например, число 27 — это третья степень: 3 ** 3, а 81 — это четвёртая: 3 ** 4.

Пример:

is_power_of_three(1)  # True
is_power_of_three(2)  # False
is_power_of_three(9)  # True
'''

def is_power_of_three(num):
  if num == 0 or num == -1:
    return False
  num = abs(num)
  while num != 1:
    if num%3 != 0:
      return False
    num /= 3
  return True

print(is_power_of_three(9))