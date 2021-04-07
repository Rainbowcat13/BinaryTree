from splay_tree import SplayTree


if __name__ == '__main__':
    tree = SplayTree()
    values = list(range(-900, 900))
    for i in values:
        tree.insert(i)
    for i in values:
        print(tree.find(i).key)

