'''
Дан список рёбер. Каждое ребро представляет собой кортеж ('Вершина 1', 'Вершина 2', Вес). Реализуйте процедуру sort(x), которая отсортирует список по возрастанию из весов:

Например, 

[('A', 'C', 3), ('B', 'C', 2), ('A', 'B', 1)]
Вернёт новый список
[('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 3)]
'''

def sort(x):
  a=[]
  for i in range(len(x)):
    a.append(x[i][2])
  copy_a = a[:]
  copy_x = x[:]
  for i in range(1, len(a)):
    j = i
    while a[j - 1] > a[j] and j > 0:
      copy_a[j - 1] = copy_a[j]
      copy_a[j] = a[j - 1]
      a = copy_a[:]
      copy_x[j - 1] = copy_x[j]
      copy_x[j] = x[j - 1]
      x = copy_x[:]
      j -= 1
  return x
  
print(sort([
    ('A', 'B', 1),
    ('B', 'C', 3),
    ('A', 'C', 2),
    ('D', 'C', 3)
]))