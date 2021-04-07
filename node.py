class Node:
    def __init__(self, key):
        self.key = key
        self.height = 0
        self.parent = None
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.key < other.key
