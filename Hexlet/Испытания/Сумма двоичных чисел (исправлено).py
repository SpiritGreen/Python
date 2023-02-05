'''
Реализуйте функцию binary_sum(), которая принимает на вход два двоичных числа (в виде строк) и возвращает их сумму. Результат (вычисленная сумма) также должен быть бинарным числом в виде строки:

binary_sum('10', '1')      # 11
binary_sum('1101', '101')  # 10010
'''

def binary_sum(a, b):
  pre_sum = int(a) + int(b)
  result = ''
  pre_sum = str(pre_sum)[::-1]
  overload = 0
  for item in pre_sum:
    if overload == 1:
      item = int(item) + 1
      overload = 0
    
    if int(item) > 1:
      overload = 1
      item = int(item) - 2
      result += str(item)
    else:
      result += str(item)
  if overload == 1:
    result += str(overload)
  return result[::-1]

print(binary_sum(11, 111))