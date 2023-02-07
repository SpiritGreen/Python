'''
Напишите фукнцию check_inheritance(), которая принимает на вход один список: наименования некоторых классов и последним элементом в списке идет название некоторого класса. Гарантируется, что некоторый класс (последний элемент в списке, переданном на вход), является наследником одного или нескольких классов из списка. Функция должна вернуть список всех родителей некоторого класса. Используйте функцию issubclass().

Примеры приводятся в формате: исходные_данные ==> результат_программы:

check_inheritance([int, str, complex, dict, bool]) ==> int

check_inheritance([object, int]) ==> object
'''

def check_inheritance(class_lst):
  result = []
  for item in class_lst:
    if item is class_lst[-1]:
      break
    if issubclass(class_lst[-1], item):
      result.append(item)
  return result

a = check_inheritance([object, int])
b = check_inheritance([int, str, complex, dict, bool])
print(a)