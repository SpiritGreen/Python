'''
В рамках этого испытания вы реализуете небольшой набор функций, работающих с отрезками прямых на двухмерной плоскости. Отрезок в нашем случае будет кодироваться в виде пары пар и выглядеть как-то так: ((x1, y1), (x2, y2)) (вложенные пары — это концы отрезка). Вам нужно реализовать четыре функции:

is_degenerated() должна возвращать истину, если отрезок вырожден в точку (начало и конец совпадают);
is_vertical() должна возвращать "истину", если отрезок — вертикальный;
is_horizontal() должна возвращать "истину", если отрезок — горизонтальный;
is_inclined() должна возвращать "истину", если отрезок — наклонный (не вертикальный и не горизонтальный).

line1 = (0, 10), (100, 130)
is_vertical(line1)  # False
is_horizontal(line1)  # False
is_degenerated(line1)  # False
is_inclined(line1)  # True

line2 = (42, 1), (42, 2)
is_vertical(line2)  # True

line3 = (100, 50), (200, 50)
is_horizontal(line3)  # True
'''

# Отрезок вырожден в точку
def is_degenerated(line):
  if line[0] == line[1]:
    return True
  else:
    return False

# Отрезок вертикальный
def is_vertical(line):
  (x1, y1) = line[0]
  (x2, y2) = line[1]
  if x1 == x2 and y1 != y2:
    return True
  else:
    return False

# Отрезок горизонтальный
def is_horizontal(line):
  (x1, y1) = line[0]
  (x2, y2) = line[1]
  if y1 == y2 and x1 != x2:
    return True
  else:
    return False

# Отрезок наклонный
def is_inclined(line):
  if not is_degenerated(line) and not is_horizontal(line) and not is_vertical(line):
    return True
  else:
    return False

    
# ПРОВЕРКА
line1 = (0, 10), (100, 130)
print(is_vertical(line1))  # False
print(is_horizontal(line1))  # False
print(is_degenerated(line1))  # False
print(is_inclined(line1))  # True

line2 = (42, 1), (42, 2)
print(is_vertical(line2))  # True

line3 = (100, 50), (200, 50)
print(is_horizontal(line3))  # True