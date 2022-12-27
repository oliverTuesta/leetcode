# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Easy
# Number: 102

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        levels = [[]]

        def addLevelNode(node, level):
            if not node:
                return
            # if level is out of range add [] to the list
            elif level >= len(levels):
                levels.append([])
            levels[level].append(node.val)
            addLevelNode(node.left, level + 1)
            addLevelNode(node.right, level + 1)
        addLevelNode(root, 0)
        
        if not levels[0]:
            return []

        return levels
