from splay_tree import SplayTree

import random
import sys

sys.setrecursionlimit(10 ** 9)


# Warning: Python has very bad recursion, so if you run splay tree on more than ~1200 elements,
# you will receive an error with code 0xC00000FD. It means you have run out of allowed stack size
# so you need to increase allowed stack size of the interpreter
class TestSplay:
    def setup_class(self):
        self.tree = SplayTree()

    def add_keys(self, keys, shuffle=False):
        if shuffle:
            random.shuffle(keys)
        for i in keys:
            self.tree.insert(i)

    def check_find(self, keys, expected_result):
        for i in keys:
            res = self.tree.find(i)
            if expected_result:
                assert res.key == i
            else:
                assert res is None

    def test_add_few_keys(self):
        keys = [1, 2, 10, 50, 100]
        self.add_keys(keys)
        self.check_find(keys, expected_result=True)
        self.check_find([111, 200, 0, 13, 44], expected_result=False)

    def test_add_many_consecutive_keys(self):
        keys = list(range(5, 5001, 5))
        self.add_keys(keys, shuffle=False)
        self.check_find(keys, expected_result=True)
        self.check_find(list(range(10000, 20000, 100)), expected_result=False)

    def test_add_many_shuffled_keys(self):
        keys = list(range(1000))
        self.add_keys(keys, shuffle=True)
        self.check_find(keys, expected_result=True)
        self.check_find(list(range(1001, 2001)), expected_result=False)

    def test_add_negative_keys(self):
        keys = list(range(-500, 501))
        self.add_keys(keys, shuffle=True)
        self.check_find(keys, expected_result=True)
        self.check_find(list(range(-1000, -500)) + list(range(501, 1001)), expected_result=False)

    def test_add_random_keys(self):
        keys = [random.randint(-1_000_000_000, 1_000_000_000) for i in range(100)]
        self.add_keys(keys)
        self.check_find(keys, expected_result=True)
        self.check_find([-(10 ** 6) - 1, 10 ** 9, 10 ** 11], expected_result=False)
