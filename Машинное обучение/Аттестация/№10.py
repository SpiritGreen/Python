'''
Напишите функцию check_instance(), которая принимает на вход один список. В списке два элемента, первый -- список, где перечислены наименования классов. Второй элемент -- некоторый объект. Функция возвращает новый список, куда собраны все наименования классов, сущностью которых является этот объект. Используйте функцию isinstance().

Примеры приводятся в формате: исходные_данные ==> результат_программы:

check_instance([[int, str, complex, dict, bool], True]) ==> int, bool

check_instance([[int, str, complex, dict], 'Hello']) ==> str
'''

def check_instance(data):
  lst = data[0]
  result = []
  for item in lst:
    if isinstance(data[-1], item):
      result.append(item)
  return result

a = check_instance([[int, str, complex, dict], 'Hello'])
print(a)