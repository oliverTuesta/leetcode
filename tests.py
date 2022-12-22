import unittest
import isomorphicStrings as ish
import isSubsequence as isub

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

if __name__ == '__main__':
    unittest.main()
