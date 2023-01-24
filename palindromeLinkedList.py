# https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy
# Number: 234

# Definition for singly-linked list.
class Listaux:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[Listaux]) -> bool:
        mid = aux = head
        n = 0
        while aux:
            if n >= 2 and n % 2 == 0:
                mid = mid.next
            aux = aux.next
            n += 1

        if n == 1:
            return True

        # reverse list from mid + 1 to end
        prev = None
        curr = mid.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr 
            if next == None:
                break;
            curr = next
        mid.next = curr

        aux = mid.next
        while head and aux:
            if head.val != aux.val:
                return False
            head = head.next
            aux = aux.next
            
        return True
