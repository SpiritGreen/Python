# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text):
    result = ''
    word = ''
    count = 0
    for item in text:
      count = count + 1
      if item == ' ':
        result = result + word[::-1] + item
        word = ''
      elif count == len(text):
        word = word + item
        result = result + word[::-1]
      else:
        word = word + item
    return result


print(reverse_words('This is an example!'))

'''
 Оптимальное решение:
 def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
'''