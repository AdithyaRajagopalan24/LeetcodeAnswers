class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        A = [0]*len(nums)
        prefix,suffix = 0,0
        for i in range(len(nums)):
            A[i] += prefix
            A[-i-1] -= suffix
            prefix += nums[i]
            suffix += nums[-i-1]
        return sum(max(0,2-abs(e)) for i,e in enumerate(A) if nums[i] == 0)
        