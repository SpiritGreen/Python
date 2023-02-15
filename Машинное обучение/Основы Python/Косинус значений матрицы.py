'''
Напишите функцию cos_array(), на вход которой передается матрица ndarray, состоящая из значений угла в градусах (0 до 360). Функция возвращает матрицу nddarray, состаящую из значений косинуса (numpy.cos). Каждый элемент матрицы нужно округлить до 2-го знака после запятой с помощью функции round(value, 2). Для обхода матрицы при округлении можно использовать вложенные циклы, размер матрицы можно узнать через поле shape у объекта ndarray.
'''

import numpy as np

def cos_array(arr):
  result = np.cos(arr)
  round_lst = []
  for vector in result:
    temp_lst = []
    for item in vector:
      item = round(item, 2)
      temp_lst.append(item)
    round_lst.append(temp_lst)
  result = np.array(round_lst)
  return result

a = np.array([[75, 31, 248],
             [345, 203, 289],
             [239, 171, 338]])
print(cos_array(a))