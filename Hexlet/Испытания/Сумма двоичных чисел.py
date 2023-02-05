'''
Реализуйте функцию binary_sum(), которая принимает на вход два двоичных числа (в виде строк) и возвращает их сумму. Результат (вычисленная сумма) также должен быть бинарным числом в виде строки:

binary_sum('10', '1')      # 11
binary_sum('1101', '101')  # 10010
'''

def binary_to_decimal(num_bin):
  # Перевернём число
  reversed_bin = str(num_bin)[::-1]
  result = 0
  power = 0
  for item in reversed_bin:
    if int(item) == 1:
      result += pow(2, power)
    power += 1
  return int(result)

def decimal_to_binary(num_dec):
  reversed_bin = ''
  while num_dec != 1:
    if num_dec%2 == 0:
      reversed_bin += '0'
    else:
      reversed_bin += '1'
    num_dec = int(num_dec/2)
  reversed_bin += str(num_dec)
  result = reversed_bin[::-1]
  return result 
      

def binary_sum(a_bin, b_bin):
  a_dec = binary_to_decimal(a_bin)
  b_dec = binary_to_decimal(b_bin)
  sum_dec = a_dec + b_dec
  sum_bin = decimal_to_binary(sum_dec)
  return sum_bin

print(binary_sum(1, 11))

