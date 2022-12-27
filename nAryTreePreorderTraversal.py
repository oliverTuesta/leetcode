# https://leetcode.com/problems/n-ary-tree-preorder-traversal
# Difficulty: Easy
# Number: 589

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        pre = []
        def addNode(node):
            if not node:
                return
            pre.append(node.val)
            if node.children:
                for child in node.children:
                    addNode(child)
        addNode(root)
        return pre
