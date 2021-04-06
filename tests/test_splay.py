import random

from splay_tree import SplayTree


class TestSplay:
    def setup_class(self):
        self.tree = SplayTree()

    def test_add_few_keys(self):
        values = [1, 2, 10, 100]
        for i in values:
            self.tree.insert(i)
        for i in values:
            assert self.tree.find(i).key == i
        assert self.tree.find(111) is None

    def test_add_many_keys(self):
        values = list(range(1000))
        random.shuffle(values)
        for i in values:
            self.tree.insert(i)
        for i in values:
            assert self.tree.find(i).key == i
        values = list(range(1001, 2001))
        for i in values:
            assert self.tree.find(i) is None

