'''
Напишите функцию create_matrix(), которая принимает на вход список списков: каждый вложенный список -- это строки матрицы (элементы вложенных списков -- целые числа). Функция создает на основе этого списка матрицу типа ndarray и возвращает ее.
'''

import numpy as np

def create_matrix(lst):
  result = np.array(lst)
  return result

print(create_matrix([[1,2,3], [1,2,3], [1,2,3]]))