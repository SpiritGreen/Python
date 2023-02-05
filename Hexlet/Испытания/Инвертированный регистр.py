'''
Реализуйте функцию invert_case(), которая меняет в строке регистр каждой буквы на противоположный.

Примеры:

invert_case('Hello, World!')  # hELLO, wORLD!
invert_case('I love Python')  # i LOVE pYTHON
'''

def invert_case(text):
  result = ''
  for item in text:
    if item.islower():
      result += item.upper()
    else:
      result += item.lower()
  return result

print(invert_case('Hello, World!'))
print(invert_case('I love Python'))