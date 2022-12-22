import unittest
import isomorphicStrings as ish

class Tests(unittest.TestCase):
    def test_ish(self):
        s = ish.Solution()
        print("test_ish:")
        self.assertEqual(s.isIsomorphic("egg", "add"), True)
        self.assertEqual(s.isIsomorphic("foo", "bar"), False)
        self.assertEqual(s.isIsomorphic("paper", "title"), True)
        self.assertEqual(s.isIsomorphic("bbbaaaba", "aaabbbba"), False)

if __name__ == '__main__':
    unittest.main()

# Output:
# $ python3 test.py
