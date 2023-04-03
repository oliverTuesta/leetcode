class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        sorted = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                sorted.append(nums1[i])
                i += 1
            else:
                sorted.append(nums2[j])
                j += 1
        if i == m:
            for e in range(j, n):
                sorted.append(nums2[e])
        else:
            for e in range(i, m):
                sorted.append(nums1[e])
        nums1[:] = sorted[:]

