def string_or_not(value):
  return type(value) == str and 'yes' or 'no'

print(string_or_not('42'))
print(string_or_not(42))