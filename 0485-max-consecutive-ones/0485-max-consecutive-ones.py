class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        curr = 0
        for x in nums:
            if x == 1:
                curr += 1
                maxCount = max(maxCount, curr)
            else:
                curr = 0
        return maxCount