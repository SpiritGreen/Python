'''
Реализуйте обход дерева в глубину по схеме: левый узел - корень - правый узел на двоичном дереве поиска. Такой обход должен порождать отсортированные последовательности, например:

dfs({
    "key": 2,
    "left": {
        "key": 1
    },
    "right": {
        "key": 3
    }
})
Печатает в консоль следующие значения

1
2
3
'''

def dfs(tree):
  if tree:
    if 'left' in tree:
      dfs(tree['left'])
    print (tree['key'])
    if 'right' in tree:
      dfs(tree['right'])


dfs({
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