'''
Дан связный список, который реализован как кортеж (число, ссылка на следующую пару) вида, в котором значения уже отсортированы:

x = (1, (3, (4, (7, (9, None)))))
Необходимо реализовать функцию, которая возвращает перевёрнутый список:
Пример вызова:

reverse((1, (3, (6, (8, None)))))
Результат:

(8, (6, (3, (1, None))))
'''

def reverse(x):
  if not x:
    return None
  current_item, lst = x
  result = None
  while current_item:
    next_item = result
    result = (current_item, next_item)
    if type(lst) == tuple:
      current_item, lst = lst
    else:
      break
  return result

x = (1, (3, (4, (7, (9, None)))))
print(reverse(x))