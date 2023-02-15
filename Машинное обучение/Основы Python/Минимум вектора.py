'''
Напишите функцию min_array(), на вход которой передается матрица ndarray, состоящая из целых чисел. Функция возвращает минимальный элемент матрицы
'''

import numpy as np

def min_array(array):
  result = np.min(array)
  return result

a = np.array([1,2,3,4])
print(min_array(a))