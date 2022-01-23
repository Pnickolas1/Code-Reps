
import math
"""

serialize and deserialize a tree


"""

# Definition for a binary tree node.
from ctypes import pointer


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        def rSerial(tree, string):

            if tree is None:
                string += 'None,'
        
            else:
                string += str(tree.val) + ','
                string = rSerial(tree.left, string)
                string = rSerial(tree.right, string)
            return string

        return rSerial(root, '')

    def deserialize(self, data):

        def rDeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rDeserialize(l)
            root.right = rDeserialize(l)
            return root
        data_list = data.split(',')
        root = rDeserialize(data_list)
        return root
