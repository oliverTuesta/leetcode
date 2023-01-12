# https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        i = 0
        while i < len(strs):
            for j in range(0, len(strs)):
                # if prefix is not in strs[j]
                if strs[j].find(prefix) != 0:
                    prefix = prefix[:-1]
                    i = j - 1
                    break
            i += 1
        return prefix
