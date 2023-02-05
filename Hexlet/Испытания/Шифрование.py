'''
Вам предстоит написать программу, которая шифрует сообщения по следующему алгоритму: она берёт текст и переставляет в нём каждые два подряд идущих символа.

Если количество символов нечётное, то последний символ остаётся на своём месте:

encrypt("move") # 'omev'
encrypt("attack") # 'taatkc'
encrypt("go!") # 'og!'
Реализуйте функцию encrypt(), который принимает на вход исходное сообщение и возвращает зашифрованное.
'''

def encrypt(message):
  result = ''
  i = 2
  length = len(message)
  while i <= length:
    string = message[(i-2):i]
    result += string[::-1]
    i += 2
  if length%2 != 0:
    result += message[-1]
  return result

print(encrypt('move'))
print(encrypt('attack'))
print(encrypt('go!'))