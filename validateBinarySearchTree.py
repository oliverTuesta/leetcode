# https://leetcode.com/problems/validate-binary-search-tree/submissions/871518303/
# Difficulty: Medium
# Number: 98

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# when convert to list, the list should be sorted to be a valid BST

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.arr = []
        self.inOrder(root)
        for i in range(1, len(self.arr)):
            if self.arr[i - 1] >= self.arr[i]:
                return False
        return True

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)

    # Another solution:
    def isValidBST2def(self, root: Optional[TreeNode]) -> bool:
        self.root = root
        return self.traverse(root)

    def validate(self, root, node):
        if root == None:
            return False
        if root == node:
            return True
        elif node.val > root.val:
            return self.validate(root.right, node)
        elif node.val < root.val:
            return self.validate(root.left, node)
        else:
            return False

    def traverse(self, node):
        if (node == None):
            return True
        v = self.validate(self.root, node)
        if not v:
            return False
        return self.traverse(node.left) and self.traverse(node.right)


