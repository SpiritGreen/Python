'''
"Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр. Номера могут быть произвольной длины, с единственным условием, что количество цифр всегда чётно, например: 33 или 2341 и так далее.

Билет с номером 385916 — счастливый, так как 3 + 8 + 5 == 9 + 1 + 6. Билет с номером 231002 не является счастливым, так как 2 + 3 + 1 != 0 + 0 + 2.

Реализуйте функцию is_happy_ticket(), проверяющую является ли номер счастливым (номер — всегда строка). Функция должна возвращать True, если билет счастливый, или False, если нет.

Примеры использования:

is_happy_ticket('123123') # True
is_happy_ticket('341800') # True

is_happy_ticket('42') # False
is_happy_ticket('12345678') # False
'''

def is_happy_ticket(number):
  half_length = len(number)/2
  index = int(half_length)
  
  first_half = number[:index]
  first_sum = 0
  
  second_half = number[-index:]
  second_sum = 0
  
  for item in first_half:
    first_sum += int(item)
  
  for item in second_half:
    second_sum += int(item)
  
  if first_sum == second_sum:
    return True
  else:
    return False

print(is_happy_ticket('341800'))