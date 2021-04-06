class Node:
    def __init__(self, key):
        self.key = key
        self.height = 0
        self.parent = None
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.key < other.key


def set_parent(v1, v2):
    if v1 is not None:
        v1.parent = v2
