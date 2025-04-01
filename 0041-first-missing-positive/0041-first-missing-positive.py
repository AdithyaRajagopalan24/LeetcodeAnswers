class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numOfVals = len(nums)
        for i in range(numOfVals):
            while 1 <= nums[i] <= numOfVals and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(numOfVals):
            if nums[i] != i + 1:
                return i + 1
        return numOfVals + 1