'''
На вход программе через input подается строка, в которой записаны элементы списка -- строки, записанные через пробел. Строки состоят из символов английского алфавита. Перейдите от строки к списку элементов. Порядок элементов менять нельзя. Создайте новый список и добавьте туда только те элементы-строки, в составе которых есть не менее трех гласных (вне зависимости от регистра). Гласные английского алфавита: a, e, i, o, u, y. Выведите итоговый список на экран. Использование функционального программирования приветствуется.

Примеры приводятся в формате: исходные_данные ==> результат_программы

'double' ==> ['double']

'LKXfFnSHVgqaU fQJrBxci sOweSnxN cQNqVHaCGinu' ==> ['cQNqVHaCGinu']
'''

def triple_vowels(lst):
  vowels = 'aeiouy'
  counter = 0
  for item in lst:
    if item.lower() in vowels:
      counter += 1
  if counter >= 3:
    return lst

data = input().split()
result = list(map(triple_vowels, data))
result = list(filter(lambda x: x != None, result))
print(result)