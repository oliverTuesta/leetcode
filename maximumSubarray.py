# https://leetcode.com/problems/maximum-subarray
# Number: 53
# Difficulty: Medium

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = 0
        sum = 0
        maxSum = nums[0]
        tail = 0
        for i in range(len(nums)):
            if nums[i] > maxSum:
                maxSum = nums[i]
            sum += nums[i]
            n += 1
            while n >= 1 and sum < 0:
                # print(subArr, sum)
                sum -= nums[tail]
                n -= 1
                tail += 1
            if sum > maxSum and n >= 1:
                maxSum = sum
        return maxSum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
