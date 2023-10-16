'''
Binary Tree
    (검색해서 사용함)
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None
