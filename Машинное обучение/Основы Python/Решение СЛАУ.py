'''
Напишите функцию solve_system(), в которую передаются: матрица коэффициентов типа ndarray и вектор свободных членов типа ndarray. Функция решает СЛАУ, описываемую представленными матрицей и вектором, и возвращает вектор -- решение СЛАУ типа ndarray.
'''

import numpy as np

def solve_system(coefficients, results_vector):
  return np.linalg.solve(coefficients, results_vector)

print(solve_system([[2.,5.], [1.,-10.]], [1.,3.]))
  