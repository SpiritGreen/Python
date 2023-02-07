'''
На вход программе через input подается строка, состоящая из символов алфавита и цифр. Выведите на экран True, если количество символов равно количеству цифр в строке. Иначе выведите False. Использование функционального программирования приветствуется.

Пример приводятся в формате: исходные_данные ==> результат_программы:

's0t0r0i0n0g0' ==> True

'5hd6f64896jd' ==> False
'''
string = input()
letter_count = len(list(filter(lambda x: x.isalpha(), string)))
number_count = len(list(filter(lambda x: x.isdigit(), string)))
if letter_count == number_count:
  print('True')
else:
  print('False')