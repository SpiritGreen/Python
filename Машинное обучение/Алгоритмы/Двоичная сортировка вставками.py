'''
Алгоритм двоичной сортировки вставками формулируется следующим образом:

Пока не пройдены все элементы списка от начала к концу взять следующий элемент в списке и с помощью бинарного поиска найти ему место в списке из элементов, стоящих до него, после чего переместить этот элемент на это место.

Реализуйте этот алгоритм, имеющий следующее описание:

def sort(x)
где x — сортируемый список.

Используйте процедуры binary_search и swap из предыдущих заданий при реализации сортировки и не забудьте добавить их в ответ, чтобы ответы были приняты. Тест проверяет, что будет отсортирован исходный список x (его можно изменить с помощью методов для работы со списками, такими как insert, pop и др.)
'''

def swap(x, old, new):
  if not x:
    return None
  element = x.pop(old)
  x.insert(new, element)
  return x

def binary_search(arr, key, start, end):
  if start > end:
    return -start - 1
  middle = (start + end) // 2
  if arr[middle] == key:
    return middle
  elif arr[middle] > key:
    end = middle - 1
    return binary_search(arr, key, start, end)
  else:
    start = middle + 1
    return binary_search(arr, key, start, end)


def sort(arr):
  i = 0
  start = 0
  while i < len(arr):
    end = i
    key = arr[i]
    new = binary_search(arr, key, start, end)
    if new != i:
      if new < 0:
        new = 0
      arr = swap(arr, i, new)
    i += 1
  return arr
  
	
x = list(map(lambda i: 20 - i, range(0, 20)))
sort(x)
print(x)