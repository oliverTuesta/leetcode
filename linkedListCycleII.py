# https://leetcode.com/problems/linked-list-cycle-ii/
# Difficulty: Medium
# Number: 142

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        memo = set()
        aux = head
        while aux:
            if aux in memo:
                return aux
            memo.add(aux)
            aux = aux.next
        return None
