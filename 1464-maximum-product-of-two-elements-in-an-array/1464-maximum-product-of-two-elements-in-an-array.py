class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstMax, secondMax = 0, 0
        for num in nums:
            if num > firstMax:
                secondMax, firstMax = firstMax, num
            else:
                secondMax = max(secondMax, num)
        return (firstMax - 1) * (secondMax - 1)