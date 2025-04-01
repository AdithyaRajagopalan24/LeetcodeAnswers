class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        finalVals, subset = [], []
        nums.sort()
        def depthFsearch(i):
            if i>=len(nums):
                finalVals.append(subset.copy())
                return
            
            subset.append(nums[i])

            depthFsearch(i+1)
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            depthFsearch(i+1)
        depthFsearch(0)
        return finalVals