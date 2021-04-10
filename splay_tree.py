from node import Node


def set_parent(v1, v2):
    if v1 is not None:
        v1.parent = v2


def keep_parents(v: Node) -> None:
    if v is None:
        return
    set_parent(v.left, v)
    set_parent(v.right, v)


def rotate(p: Node, v: Node) -> None:
    g = p.parent
    if g is not None:
        if g.left == p:
            g.left = v
        else:
            g.right = v
    set_parent(v, g)
    if p.left == v:
        p.left = v.right
        set_parent(v.right, p)
        v.right = p
        set_parent(p, v)
    else:
        p.right = v.left
        set_parent(v.left, p)
        v.left = p
        set_parent(p, v)
    keep_parents(v)
    keep_parents(p)
    v.parent = g


class SplayTree:
    def __init__(self):
        self.root = None

    def _recount_heights(self, v):
        if v is None:
            return 0
        v.height = max(self._recount_heights(v.left),
                       self._recount_heights(v.right)) + 1
        return v.height

    def _splay(self, v):
        if v.parent is None:
            return v
        p = v.parent
        g = p.parent
        if g is None:
            rotate(p, v)
            return v
        else:
            zigzig = (g.left == p) == (p.left == v)
            if zigzig:
                rotate(g, p)
                rotate(p, v)
            else:
                rotate(p, v)
                rotate(g, v)
            return self._splay(v)

    def _find_by_key(self, v, key):
        if v is None:
            return None
        if key == v.key:
            return self._splay(v)
        elif key < v.key:
            return self._find_by_key(v.left, key)
        else:
            return self._find_by_key(v.right, key)

    def _find_nearest(self, v, key):
        if key < v.key and v.left is not None:
            return self._find_nearest(v.left, key)
        elif key > v.key and v.right is not None:
            return self._find_nearest(v.right, key)
        return self._splay(v)

    def _split(self, v, key):
        if v is None:
            return None, None
        cur = self._find_nearest(v, key)
        if cur.key == key:
            set_parent(cur.left, None)
            set_parent(cur.right, None)
            return cur.left, cur.right
        elif cur.key < key:
            right = cur.right
            cur.right = None
            set_parent(right, None)
            return cur, right
        else:
            left = cur.left
            cur.left = None
            set_parent(left, None)
            return left, cur

    def _merge(self, left, right):
        if right is None:
            return left
        if left is None:
            return right
        right = self._find_nearest(right, left.key)
        right.left = left
        left.parent = right
        return right

    def insert(self, key: int) -> None:
        parts = self._split(self.root, key)
        new_root = Node(key)
        new_root.left = parts[0]
        new_root.right = parts[1]
        keep_parents(new_root)
        self.root = new_root
        self._recount_heights(self.root)

    def remove(self, key: int) -> None:
        v = self._find_by_key(self.root, key)
        if v is None:
            return
        set_parent(v.left, None)
        set_parent(v.right, None)
        self.root = self._merge(v.left, v.right)
        self._recount_heights(self.root)

    def find(self, key: int) -> Node:
        result = self._find_by_key(self.root, key)
        if result is not None:
            self.root = result
            self._recount_heights(self.root)
        return result

    def clear(self):
        self.root = None
