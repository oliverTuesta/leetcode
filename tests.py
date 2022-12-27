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
import arrayPartition as ap
import moveZeroes as mz
import maximumRepeatingSubstring as mrs
import bestTimeToBuyAndSellStock as btbs
import longestPalindrome as lp
import squaresOfSortedArray as sosa
import rotateArray as ra
import nAryTreePreorderTraversal as ntpt
import binaryTreeLevelOrderTraversal as btlot
import twoSumII as tsii
import reverseString as rs

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

class TestAp(unittest.TestCase):
    def test_ap(self):
        s = ap.Solution()
        self.assertEqual(s.arrayPairSum([1,4,3,2]), 4)
        self.assertEqual(s.arrayPairSum([6,2,6,5,1,2]), 9)

class TestMoveZeroes(unittest.TestCase):
    def test_mz(self):
        s = mz.Solution()
        nums = [0,1,0,3,12]
        s.moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])
        nums = [0,0,1]
        s.moveZeroes(nums)
        self.assertEqual(nums, [1,0,0])

class TestMaximumRepeatingSubstring(unittest.TestCase):
    def test_mrs(self):
        s = mrs.Solution()
        self.assertEqual(s.maxRepeating("ababc", "ab"), 2)
        self.assertEqual(s.maxRepeating("ababc", "ba"), 1)
        self.assertEqual(s.maxRepeating("ababc", "ac"), 0)
        self.assertEqual(s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"), 5)

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_btbs(self):
        s = btbs.Solution()
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(s.maxProfit([7,6,4,3,1]), 0)
        self.assertEqual(s.maxProfit([2,4,1]), 2)
        self.assertEqual(s.maxProfit([5,4,3,2,5,3,2,10,1,10]), 9)

class TestLongestPalindrome(unittest.TestCase):
    def test_lp(self):
        s = lp.Solution()
        self.assertEqual(s.longestPalindrome("abccccdd"), 7)
        self.assertEqual(s.longestPalindrome("a"), 1)
        self.assertEqual(s.longestPalindrome("abcd"), 1)
        self.assertEqual(s.longestPalindrome("ac"), 1)
        self.assertEqual(s.longestPalindrome("aaaaaaaaaaaaaaaa"), 16)
        self.assertEqual(s.longestPalindrome("aaaabaaaa"), 9)

class TestSquaresOfSortedArray(unittest.TestCase):
    def test_sosa(self):
        s = sosa.Solution()
        self.assertEqual(s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

class TestRotateArray(unittest.TestCase):
    def test_ra(self):
        s = ra.Solution()
        nums = [1,2,3,4,5,6,7]
        s.rotate(nums, 3)
        self.assertEqual(nums, [5,6,7,1,2,3,4])
        nums = [-1,-100,3,99]
        s.rotate(nums, 2)
        self.assertEqual(nums, [3,99,-1,-100])
        nums = [1,2,3,4,5,6,7]
        s.rotate(nums, 8)
        self.assertEqual(nums, [7,1,2,3,4,5,6])

class TestNAryTreePreorderTraversal(unittest.TestCase):
    def test_ntpt(self):
        s = ntpt.Solution()
        root = ntpt.Node(1)
        root.children = [ntpt.Node(3), ntpt.Node(2), ntpt.Node(4)]
        root.children[0].children = [ntpt.Node(5), ntpt.Node(6)]
        self.assertEqual(s.preorder(root), [1,3,5,6,2,4])

class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def test_btlot(self):
        s = btlot.Solution()
        root = btlot.TreeNode(3)
        root.left = btlot.TreeNode(9)
        root.right = btlot.TreeNode(20)
        root.right.left = btlot.TreeNode(15)
        root.right.right = btlot.TreeNode(7)
        self.assertEqual(s.levelOrder(root), [[3],[9,20],[15,7]])
        
        root = btlot.TreeNode(1)
        root.left = btlot.TreeNode(2)
        root.right = btlot.TreeNode(3)
        root.left.left = btlot.TreeNode(4)
        root.left.right = btlot.TreeNode(5)
        self.assertEqual(s.levelOrder(root), [[1],[2,3],[4,5]])

        root = btlot.TreeNode(1)
        self.assertEqual(s.levelOrder(root), [[1]])

        self.assertEqual(s.levelOrder(None), [])

class TestTwoSumII(unittest.TestCase):
    def test_ts(self):
        s = tsii.Solution()
        self.assertEqual(s.twoSum([2,7,11,15], 9), [1,2])
        self.assertEqual(s.twoSum([2,3,4], 6), [1,3])
        self.assertEqual(s.twoSum([-1,0], -1), [1,2])
        self.assertEqual(s.twoSum([0,0,3,4], 0), [1,2])

class TestReverseString(unittest.TestCase):
    def test_rs(self):
        s = rs.Solution()
        aux = ["h","e","l","l","o"]
        s.reverseString(aux)
        self.assertEqual(aux, ["o","l","l","e","h"]
)
        aux = ["H","a","n","n","a","h"]
        s.reverseString(aux)
        self.assertEqual(aux, ["h","a","n","n","a","H"])
        aux = ["a"]
        s.reverseString(aux)
        self.assertEqual(aux, ["a"])
        aux = ["a","b"]
        s.reverseString(aux)
        self.assertEqual(aux, ["b","a"])

if __name__ == '__main__':
    unittest.main()
