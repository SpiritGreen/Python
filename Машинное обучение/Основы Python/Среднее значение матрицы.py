'''
Напишите функцию mean_array(), на вход которой передается матрица ndarray, состоящая из целых чисел. Функция возвращает среднее значение по матрице, округленное до 2-х знаков после запятой с помощью функции round(value , 2).
'''

import numpy as np

def mean_array(arr):
  result = np.mean(arr)
  result = round(result, 2)
  return result