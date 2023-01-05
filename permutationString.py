# https://leetcode.com/problems/permutation-in-string/?envType=study-plan&id=algorithm-i
# Difficulty: Medium
# Number: 567

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = dict()
        for c in s1:
            chars[c] = chars.get(c, 0) + 1

        count = 0
        remaining_chars = chars.copy()
        for i in range(0, len(s2)):
            if s2[i] in remaining_chars:
                if remaining_chars[s2[i]] == 0:
                    j = i - count
                    while count > 0 and remaining_chars[s2[i]] == 0:
                        count = count - 1
                        remaining_chars[s2[j]] = remaining_chars[s2[j]] + 1
                        j = j + 1
                count = count + 1
                remaining_chars[s2[i]] = remaining_chars[s2[i]] - 1
            else:
                count = 0
                remaining_chars = chars.copy()
            if count == len(s1):
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))
    print(s.checkInclusion("adc", "dcda"))
