'''
Напишите функцию get_info(), которая принимает на вход матрицу ndarray чисел и возвращает количество строк и столбцов в ней в виде кортежа: (количество строк, количество столбцов)
'''

def get_info(matrix):
  line_count = len(matrix)
  column_count = len(matrix[0])
  return (line_count, column_count)

print(get_info([[1,2,3], [1,2,3], [1,2,3]]))