'''
Используя функциональное программирование решите следующую задачу. Напишите функцию solve(obj), которая принимает на вход список строк и возвращает список, в котором содержатся только те элементы исходного списка, которые начинаются с прописной буквы и не включают цифр. При решении обратите внимание, что:

Функция не должна ничего выводить на экран.
Кроме определения функции ничего другого писать не нужно.
Использование функционального программирования приветствуется.
Примеры приводятся в формате: исходные_данные ==> результат_программы:

solve(['ADSiR', 'HPfAm', 'xd4fcFH', 'SxyIJd']) ==> ['ADSiR', 'HPfAm', 'SxyIJd']

solve(['zUHfBaNV', 'VIF9x', 'OkOeLg']) ==> ['OkOeLg']
'''

def filter_lst(lst):
  if not (lst[0].isalpha() and lst[0].isupper()):
    return None
  for item in lst:
    if item.isalpha():
      continue
    else:
      return None
  return lst
  
def solve(lst):
  result = list(filter(filter_lst, lst))
  result = list(filter(lambda x: x!=None, result))
  return result

print(solve(['ADSiR', 'HPfAm', 'xd4fcFH', 'SxyIJd']))
  