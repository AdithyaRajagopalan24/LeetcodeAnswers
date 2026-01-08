class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def maxProductFrom(i: int, j: int) -> int:
            if i == len(nums1) or j == len(nums2):
                return 0

            takeBoth = nums1[i] * nums2[j] + maxProductFrom(i + 1, j + 1)
            skipBoth = maxProductFrom(i + 1, j + 1)
            skipNums1 = maxProductFrom(i + 1, j)
            skipNums2 = maxProductFrom(i, j + 1)

            return max(takeBoth, skipBoth, skipNums1, skipNums2)

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return maxProductFrom(0, 0)
