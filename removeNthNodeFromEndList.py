# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Number: 19

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):

        self.ans = head

        def nReverseNode(node, n, target):
            if (node == None):
                return 0
            nReverse = nReverseNode(node.next, n + 1, target) + 1
            # if the node that i want to remove is the first one
            if nReverse == target and n == 1:
                self.ans = node.next
            elif nReverse - 1 == target:
                node.next = node.next.next
            return nReverse

        nReverseNode(head, 1, n)
        return self.ans


