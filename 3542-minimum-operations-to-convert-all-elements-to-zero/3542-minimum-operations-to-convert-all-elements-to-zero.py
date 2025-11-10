class Solution:
    def minOperations(self, nums):
        stack = [0] * (len(nums) + 1)
        topVal = 0
        finalVal = 0

        for num in nums:
            while stack[topVal] > num:
                topVal -= 1
                finalVal += 1
            if stack[topVal] != num:
                topVal += 1
                stack[topVal] = num
        return finalVal + topVal