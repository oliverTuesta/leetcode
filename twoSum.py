# https://leetcode.com/problems/two-sum
# Number: 1
# Difficulty: Easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        m = {}
        for i in range(len(nums)):
            if target - nums[i] in m:
                ans.append(m[target - nums[i]])
                ans.append(i)
                return ans
            m[nums[i]] = i
        return ans


