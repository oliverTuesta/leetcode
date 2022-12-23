# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Number: 21

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        aux = head
        while list1 and list2:
            if list1.val < list2.val:
                aux.next = list1
                aux = list1
                list1 = list1.next
            else:
                aux.next = list2
                aux = list2
                list2 = list2.next

        if list1:
            aux.next = list1
        elif list2:
            aux.next = list2

        return head.next
