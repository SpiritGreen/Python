'''
Дан связный список, который реализован как кортеж (число, ссылка на следующую пару) вида:

x = (1, (2, (3, (4, (5, None)))))
Реализовать функцию добавления нового элемента в начало очереди, которая принимает на вход число и первый элемент списка и возвращает новый список, в котором первый элемент содержит переданное число и ссылку на следующий узел:
Пример вызова:

prepend(1, (3, None))

Результат:

(1, (3, None))
'''

def prepend(item, lst):
  result = (item, lst)
  return result

x = (1, (2, (3, (4, (5, None)))))
print(prepend(1, x))