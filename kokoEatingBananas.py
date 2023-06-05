# https://leetcode.com/problems/koko-eating-bananas/
import math

class Solution:
    def can_eat_all_bananas(self, piles: list[int], h: int, k: int) -> bool:
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / k)
            if hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0

        while (left <= right):
            middle = (right + left) // 2
            if self.can_eat_all_bananas(piles, h, middle):
                right = middle - 1
                ans = middle
            else:
                left = middle + 1

        return ans

def main():
    print("TESTING KOKO EATING BANANAS...")
    test_solution = Solution()
    test_piles = [3, 6, 7, 11]
    test_h = 8
    print(test_solution.minEatingSpeed(test_piles, test_h))

    test_piles = [30, 11, 23, 4, 20]
    test_h = 5
    print(test_solution.minEatingSpeed(test_piles, test_h))

    test_piles = [30, 11, 23, 4, 20]
    test_h = 6
    print(test_solution.minEatingSpeed(test_piles, test_h))

    test_piles = [312884470]
    test_h = 312884469
    print(test_solution.minEatingSpeed(test_piles, test_h))

    print("END OF TESTING...")
    return 0

main()
