'''
Напишите функцию vsum_array(), на вход которой передается матрица ndarray, состоящая из целых чисел. Функция возвращает ndarray-вектор, содержащий значения сумм элементов по столбцам.
'''
import numpy as np

def vsum_array(array):
  result = np.sum(array, axis = 0)
  return result

a = np.array([[1,2], [3, 4], [5, 6]])
print(vsum_array(a))