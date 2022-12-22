# https://leetcode.com/problems/isomorphic-strings/
# Number: 205
# Difficulty: Easy

class Solution(object):
    def isIsomorphic(self, s, t):
        mapS = dict()
        mapT = dict()
        for i in s:
            if i not in mapS:
                mapS[i] = 1
            else:
                mapS[i] = mapS[i] + 1
        for i in t:
            if i not in mapT:
                mapT[i] = 1
            else:
                mapT[i] = mapT[i] + 1
        aux = {}
        for i in range(0, len(s)):
            if s[i] not in aux:
                aux[s[i]] = ord(s[i]) - ord(t[i]);
            elif ord(s[i]) - ord(t[i]) != aux[s[i]]:
                return False
            if mapS.get(s[i]) != mapT.get(t[i]):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("egg", "add"))
    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))
    print(s.isIsomorphic("bbbaaaba", "aaabbbba"))
