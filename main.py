from splay_tree import SplayTree


if __name__ == '__main__':
    tree = SplayTree()
    keys = [-10, 15, 42, 11, 7, 100009, -300]
    for i in keys:
        tree.insert(i)
    for i in [1, 2, 3, 4, 5]:
        tree.remove(i)
    for i in keys[:3]:
        tree.remove(i)
    for i in keys[:3]:
        print(tree.find(i))
    print()
    for i in keys[3:]:
        print(tree.find(i).key)

