'''
Напишите функцию diff, которая принимает два угла (int) и возвращает наименьшую разницу между ними.
'''

def diff(ang1, ang2):
  # Приведём углы к нормальному виду
  ang1 = abs(ang1)%360
  ang2 = abs(ang2)%360
  # Найдём разницу
  result = abs(ang1 - ang2)
  if result > 180:
    return 360 - result
  else:
    return result

print(diff(120, 280))