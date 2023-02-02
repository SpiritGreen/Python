'''
Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным. Год будет високосным, если он делится без остатка на 400, или он одновременно делится без остатка на 4 и не делится на 100:

is_leap_year(2018)  # False
is_leap_year(2017)  # False
is_leap_year(2016)  # True

'''

def is_leap_year(year):
  return year%400==0 or (year%4==0 and year%100!=0)

print(is_leap_year(2018))