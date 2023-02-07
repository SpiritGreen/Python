'''
На вход подается строка, в которой записаны элементы списка -- целые числа через пробел. Перейдите от строки к списку объектов типа int. Создайте новый список и добавьте в него только те числа из исходного списка, которые делятся без остатка на хотя бы одно другое число из этого же списка. Выведите новый список на экран. В итоговом списке должны быть объекты типа int. Использование функционального программирования приветствуется.

Примеры приводятся в формате: исходные_данные ==> результат_программы:

'3 2 6' ==> [6]

'4 2 8' ==> [4, 8]
'''

numbers = input().split()
numbers = list(map(lambda x: int(x), numbers))
result = []
for item in numbers:
  for num in numbers:
    if num == 0:
      continue
    elif (item != num) and item%num==0:
      result.append(item)
      break
print(result)