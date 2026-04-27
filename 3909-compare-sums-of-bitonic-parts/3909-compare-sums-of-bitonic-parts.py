class Solution:
    def compareBitonicSums(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if 0 < mid < len(nums) - 1 and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                break
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        leftSum = sum(nums[:mid + 1])
        rightSum = sum(nums[mid:])

        if leftSum > rightSum:
            return 0
        elif rightSum > leftSum:
            return 1
        return -1