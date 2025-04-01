class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # minVal = min(nums)
        # maxVal = max(nums)
        # tagCount = maxVal - minVal + 2
        # tags = [[] for i in range(tagCount)]
        # for i in nums:
        #     tags[i].append(i)
        # finalList = []
        # for i in tags:
        #     finalList.extend(i)
        maxSum = 0
        nums.sort()
        for i in range(len(nums)):
            if i%2==0:
                maxSum += nums[i]
        return maxSum