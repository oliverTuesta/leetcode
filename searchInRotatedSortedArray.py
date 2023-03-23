# https://leetcode.com/problems/search-in-rotated-sorted-array
# Difficulty: Medium
# Number: 33

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = self.findPivot(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[(m - pivot) % len(nums)] == target:
                return (m - pivot) % len(nums)
            elif nums[(m - pivot) % len(nums)] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

    def findPivot(self, nums: list[int]) -> int:
        if len(nums) == 1 or (nums[0] < nums[-1]):
            return 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return len(nums) - i
        return 0;

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2], 0))
    print(solution.search([4,5,6,7,0,1,2], 3))
    print(solution.search([1], 0))
    print(solution.search([3,5,1], 5))
    print(solution.search([3, 1], 1))
