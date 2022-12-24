# https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy
# Number: 876

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        aux = middle = head
        count = 0
        while aux:
            count = count + 1
            if count % 2 == 0:
                middle = middle.next
            aux = aux.next
        return middle


