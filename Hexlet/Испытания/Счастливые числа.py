'''
Назовем счастливыми числами те, которые в результате ряда преобразований вида сумма квадратов цифр превратятся в единицу. Например:

7   -> 7^2 = 49
49  -> 4^2 + 9^2 = 97
97  -> 9^2 + 7^2 = 130
130 -> 1^2 + 3^2 + 0^2 = 10
10  -> 1^2 + 0^2 = 1
Вывод: исходное число 7 - счастливое.

Реализуйте функцию is_happy_number(), которая возвращает True, если число счастливое, и False, если нет. Количество итераций процесса поиска необходимо ограничить числом 10.

Воспользуйтесь вспомогательной функцией sum_of_square_digits(), которая принимает на вход число и возвращает сумму квадратов цифр этого числа.
'''

def sum_of_square_digits(num):
  result = 0
  for item in str(num):
    result += int(item)**2
  return result

def is_happy_number(num):
  i = 0
  result = sum_of_square_digits(num)
  while i < 10:
    if result == 1:
      return True
    else:
      result = sum_of_square_digits(result)
  return False

print(is_happy_number(7))