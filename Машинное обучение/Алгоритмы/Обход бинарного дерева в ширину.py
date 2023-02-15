'''
Реализуйте обход дерева в ширину. Такой обход должен порождать последовательности значений как при обходе дерева сверху вниз, слева направо, т.е.

bfs({
    "key": 2,
    "left": {
        "key": 1
    },
    "right": {
        "key": 3
    }
})
печатает в консоль следующие значения

2
1
3
'''

def bfs(tree):
  if tree:
    a = [tree]
    while len(a) > 0:
      b = a.pop(0)
      print(b['key'])
      if 'left' in b:
        a.append(b['left'])
      if 'right' in b:
        a.append(b['right'])

bfs({
    'key': 8,
    'left': {
        'key': 6,
        'left': {
            'key': 3,
            'left': {
                'key': 1
            },
            'right': {
                'key': 4
            }
        }
    },
    'right': {
        'key': 12,
        'left': {
            'key': 9
        },
        'right': {
            'key': 15
        }
    }
})