class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sumNums1, zeroCount1 = 0, 0
        sumNums2, zeroCount2 = 0, 0
        for num in nums1:
            if num == 0:
                zeroCount1 += 1
            else:
                sumNums1 += num
        for num in nums2:
            if num == 0:
                zeroCount2 += 1
            else:
                sumNums2 += num
        totalSum1 = sumNums1 + zeroCount1
        totalSum2 = sumNums2 + zeroCount2
        if zeroCount1 == 0 and sumNums1 < totalSum2:
            return -1
        if zeroCount2 == 0 and sumNums2 < totalSum1:
            return -1
        return max(totalSum1, totalSum2)
