# https://leetcode.com/problems/cousins-in-binary-tree/
# Number: 993
# Difficulty: easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def helper(node, parent, depth):
            if node == None:
                return
            if node.val == x:
                self.x_depth = depth + 1
                self.x_parent = parent
            if node.val == y:
                self.y_depth = depth + 1
                self.y_parent = parent
            helper(node.left, node, depth + 1)
            helper(node.right, node, depth + 1)

        self.x_depth = -1
        self.x_parent = None
        self.y_depth = -1
        self.y_parent = None
        helper(root, None, -1)
        print(self.x_depth, self.y_depth)
        cousins = self.x_depth == self.y_depth and self.x_parent != self.y_parent
        return cousins

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(s.isCousins(root, 5, 4))

