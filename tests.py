import unittest
import isomorphicStrings as ish
import isSubsequence as isub
import mergeTwoSortedLists as mtsl

class TestIsh(unittest.TestCase):
    def test_ish(self):
        s = ish.Solution()
        print("test_ish:")
        self.assertEqual(s.isIsomorphic("egg", "add"), True)
        self.assertEqual(s.isIsomorphic("foo", "bar"), False)
        self.assertEqual(s.isIsomorphic("paper", "title"), True)
        self.assertEqual(s.isIsomorphic("bbbaaaba", "aaabbbba"), False)

class TestIsub(unittest.TestCase):
    def test_subs(self):
        s = isub.Solution()
        print("Is Subsequence:")
        self.assertEqual(s.isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(s.isSubsequence("axc", "ahbgdc"), False)
        self.assertEqual(s.isSubsequence("fdas", "fufdfasjfkingasasdas"), True)
        self.assertEqual(s.isSubsequence("", "ahbgdc"), True)
        self.assertEqual(s.isSubsequence("b", "c"), False)

class TestMtsl(unittest.TestCase):
    def test_mtsl(self):
        s = mtsl.Solution()
        print("Merge Two Sorted Lists:")
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


if __name__ == '__main__':
    unittest.main()
