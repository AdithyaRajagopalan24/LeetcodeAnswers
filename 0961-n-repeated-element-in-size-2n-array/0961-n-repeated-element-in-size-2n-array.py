class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(i, min(n-1, i+3)):
                if nums[i] == nums[j+1]: return nums[i]