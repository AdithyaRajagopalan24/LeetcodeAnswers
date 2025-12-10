class Solution:
    def countPermutations(self, nums: List[int]) -> int:
        finalVal = 1
        MOD = pow(10,9)+7
        baseVal = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= baseVal:
                finalVal = 0
                break
            finalVal = (finalVal * i) % MOD
        return finalVal