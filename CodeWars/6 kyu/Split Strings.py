'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''

def solution(s):
  result = []
  if not s:
    return result
  else:
    symbol_counter = 0
    for item in s:
      symbol_counter +=1
      if (symbol_counter == len(s)) and (len(s)%2 != 0):
        result.append(item + '_')
      elif symbol_counter%2 != 0:
        symbols = item
      else:
        symbols += item
        result.append(symbols)
  return result

print(solution('abcdef'))

'''
Оптимальное решение:

def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
    
'''
        