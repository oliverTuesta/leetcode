# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/871544903/
# Difficulty: Medium
# Number: 235

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class       Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findLowest(root, p, q)

    def findLowest(self, root, p, q) -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.findLowest(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.findLowest(root.left, p, q)
        elif root == p or root == q:
            return root
        else:
            return root
