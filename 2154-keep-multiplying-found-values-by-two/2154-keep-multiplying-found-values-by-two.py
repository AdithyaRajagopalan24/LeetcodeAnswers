class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        countVals = [0] * 1001
        for x in nums:
            countVals[x] += 1

        while original <= 1000 and countVals[original] > 0:
            original *= 2

        return original