'''
Дан связный список, который реализован как кортеж (число, ссылка на следующую пару) вида:

x = (1, (2, (3, (4, (5, None)))))
Необходимо написать функцию iter(x), который печатает элементы списка:

Вызов:

iter((1, (2, (3, (4, (5, None))))))

Результат:

1
2
3
4
5
'''

def iter(x):
  items = x
  if not items:
    return None
  current_item, next_item = items
  while current_item:
    print(current_item)
    items = next_item
    if type(items) == tuple:
      current_item, next_item = items
    else:
      break
    

x = (1, (2, (3, (4, (5, None)))))

print(iter(None))