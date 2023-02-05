'''
Реализуйте функцию fib(), находящую положительные Числа Фибоначчи. Аргументом функции является порядковый номер числа.

Формула:
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)

fib(3)  # 2
fib(5)  # 5
fib(10)  # 55
'''
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    current = 0
    next = 1
    index = 2
    while index <= n:
      # print(next)
      (current, next) = (next, current + next)
      index += 1
    return next

print(fib(11))