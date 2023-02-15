'''
Реализуйте процедуру mst(x), которая принимает на вход список рёбер графа с весом и возвращает список только из тех ребёр, которые входят в минимальное основное дерево в порядке возрастания весов:

mst([('A', 'C', 3), ('B', 'C', 2), ('A', 'B', 1)])
Возвращает список

[('A', 'B', 1), ('B', 'C', 2)]
Чтобы ответ был принят необходимо добавить процедуры сортировки и поиска в системе непересекающихся множеств.
'''

def mst(x):
  a=[]
  for i in range(len(x)):
    a.append(x[i][2])
  copy_a = a[:]
  copy_x = x[:]
  for i in range(1, len(a)):
    j = i
    while a[j - 1] > a[j] and j > 0:
      copy_a [j - 1] = copy_a [j]
      copy_a [j] = a [j - 1]
      a = copy_a[:]
      copy_x [j - 1] = copy_x [j]
      copy_x [j] = x [j - 1]
      x = copy_x[:]
      j -= 1
  answer = []
  previous = []
  for i in range(len(x)):
    if (not (x[i][0] in previous and x[i][1] in previous) and x[i][0] != x[i][1]):
      answer.append(x[i])
      previous.append(x[i][0])
      previous.append(x[i][1])
  return answer

	
print(mst([
    ('A', 'B', 1),
    ('B', 'C', 3),
    ('A', 'C', 2),
    ('D', 'C', 3)
]))