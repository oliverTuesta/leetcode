# https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = m - 1
            else: 
                l = m + 1
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


