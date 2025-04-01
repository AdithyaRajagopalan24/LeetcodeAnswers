class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        minCount = len(nums)/2
        maxNum = 0
        dictOfFreq = {}
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i not in list(dictOfFreq.keys()):
                dictOfFreq[i] = 1
            else:
                dictOfFreq[i] += 1
                if dictOfFreq[i] > minCount:
                    maxNum = i
        return maxNum