from splay_tree import SplayTree

import sys
sys.setrecursionlimit(10 ** 9)


if __name__ == '__main__':
    tree = SplayTree()
    values = list(range(1000))
    for i in values:
        tree.insert(i)
    for i in values:
        print(tree.find(i).key)

