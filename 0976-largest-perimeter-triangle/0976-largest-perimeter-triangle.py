class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            num3rd, num2nd, num1st = nums[i-2], nums[i-1], nums[i]
            if num3rd + num2nd > num1st:
                return num3rd + num2nd + num1st
        return 0