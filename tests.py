import unittest
import isomorphicStrings as ish
import isSubsequence as isub
import mergeTwoSortedLists as mtsl
import reverseLinkedList as rll
import binarySearch as bs
import firstBadVersion as fbv
import searchInsertPosition as sip
import middleOfTheLinkedList as moll
import linkedListCycleII as llcii

class TestIsh(unittest.TestCase):
    def test_ish(self):
        s = ish.Solution()
        self.assertEqual(s.isIsomorphic("egg", "add"), True)
        self.assertEqual(s.isIsomorphic("foo", "bar"), False)
        self.assertEqual(s.isIsomorphic("paper", "title"), True)
        self.assertEqual(s.isIsomorphic("bbbaaaba", "aaabbbba"), False)

class TestIsub(unittest.TestCase):
    def test_subs(self):
        s = isub.Solution()
        self.assertEqual(s.isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(s.isSubsequence("axc", "ahbgdc"), False)
        self.assertEqual(s.isSubsequence("fdas", "fufdfasjfkingasasdas"), True)
        self.assertEqual(s.isSubsequence("", "ahbgdc"), True)
        self.assertEqual(s.isSubsequence("b", "c"), False)

class TestMtsl(unittest.TestCase):
    def test_mtsl(self):
        s = mtsl.Solution()
        l1 = mtsl.ListNode(1)
        l1.next = mtsl.ListNode(2)
        l1.next.next = mtsl.ListNode(4)
        l2 = mtsl.ListNode(1)
        l2.next = mtsl.ListNode(3)
        l2.next.next = mtsl.ListNode(4)
        l3 = s.mergeTwoLists(l1, l2)
        self.assertEqual(l3.val, 1)
        self.assertEqual(l3.next.val, 1)
        self.assertEqual(l3.next.next.val, 2)
        self.assertEqual(l3.next.next.next.val, 3)
        self.assertEqual(l3.next.next.next.next.val, 4)
        self.assertEqual(l3.next.next.next.next.next.val, 4)
        self.assertEqual(l3.next.next.next.next.next.next, None)

class TestRll(unittest.TestCase):
    def test_rll(self):
        s = rll.Solution()
        l1 = rll.ListNode(1)
        l1.next = rll.ListNode(2)
        l1.next.next = rll.ListNode(3)
        l1.next.next.next = rll.ListNode(4)
        l1.next.next.next.next = rll.ListNode(5)
        l2 = s.reverseList(l1)
        self.assertEqual(l2.val, 5)
        self.assertEqual(l2.next.val, 4)
        self.assertEqual(l2.next.next.val, 3)
        self.assertEqual(l2.next.next.next.val, 2)
        self.assertEqual(l2.next.next.next.next.val, 1)
        self.assertEqual(l2.next.next.next.next.next, None)

class TestBs(unittest.TestCase):
    def test_bs(self):
        s = bs.Solution()
        self.assertEqual(s.search([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(s.search([-1,0,3,5,9,12], 2), -1)
        self.assertEqual(s.search([5], 5), 0)
        self.assertEqual(s.search([2,5], 5), 1)
        self.assertEqual(s.search([2,5], 2), 0)
        self.assertEqual(s.search([2,5], 6), -1)
        self.assertEqual(s.search([2,5], 1), -1)

class TestFbv(unittest.TestCase):
    def test_fbv(self):
        s = fbv.Solution()
        self.assertEqual(s.firstBadVersion(5), 4)
        self.assertEqual(s.firstBadVersion(4), 4)
        self.assertEqual(s.firstBadVersion(15), 4)
        self.assertEqual(s.firstBadVersion(5), 4)
        self.assertEqual(s.firstBadVersion(1004), 4)
        self.assertEqual(s.firstBadVersion(412034), 4)

class TestSib(unittest.TestCase):
    def test_sib(self):
        s = sip.Solution()
        self.assertEqual(s.searchInsert([1,3,5,6], 5), 2)
        self.assertEqual(s.searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(s.searchInsert([1,3,5,6], 7), 4)
        self.assertEqual(s.searchInsert([-5, -4, 0, 1,3,5,6], -6), 0)
        self.assertEqual(s.searchInsert([1,3,5,6], 49), 4)
        self.assertEqual(s.searchInsert([1,3,5,6], 0), 0)

class TestMoll(unittest.TestCase):
    def test_moll(self):
        s = moll.Solution()
        l1 = moll.ListNode(1)
        l1.next = moll.ListNode(2)
        l1.next.next = moll.ListNode(3)
        l1.next.next.next = moll.ListNode(4)
        l1.next.next.next.next = moll.ListNode(5)
        l2 = s.middleNode(l1)
        self.assertEqual(l2.val, 3)
        self.assertEqual(l2.next.val, 4)
        self.assertEqual(l2.next.next.val, 5)
        self.assertEqual(l2.next.next.next, None)

class TestLlcII(unittest.TestCase):
    def test_llcII(self):
        s = llcii.Solution()
        l1 = llcii.ListNode(3)
        l1.next = llcii.ListNode(2)
        l1.next.next = llcii.ListNode(0)
        l1.next.next.next = llcii.ListNode(4)
        l1.next.next.next.next = l1.next
        ans = s.detectCycle(l1)
        self.assertEqual(ans, l1.next)

        l2 = llcii.ListNode(1)
        l2.next = llcii.ListNode(2)
        l2.next.next = l2
        ans = s.detectCycle(l2)
        self.assertEqual(ans, l2)

        l3 = llcii.ListNode(1)
        l3.next = llcii.ListNode(2)
        l3.next.next = llcii.ListNode(3)
        ans = s.detectCycle(l3)
        self.assertEqual(ans, None)

        #[-1,-7,7,-4,19,6,-9,-5,-2,-5]
        l4 = llcii.ListNode(-1)
        l4.next = llcii.ListNode(-7)
        l4.next.next = llcii.ListNode(7)
        l4.next.next.next = llcii.ListNode(-4)
        l4.next.next.next.next = llcii.ListNode(19)
        l4.next.next.next.next.next = llcii.ListNode(6)
        l4.next.next.next.next.next.next = llcii.ListNode(-9)
        l4.next.next.next.next.next.next.next = llcii.ListNode(-5)
        l4.next.next.next.next.next.next.next.next = llcii.ListNode(-2)
        l4.next.next.next.next.next.next.next.next.next = l4.next.next.next.next.next.next
        ans = s.detectCycle(l4)
        self.assertEqual(ans, l4.next.next.next.next.next.next)

 


if __name__ == '__main__':
    unittest.main()
