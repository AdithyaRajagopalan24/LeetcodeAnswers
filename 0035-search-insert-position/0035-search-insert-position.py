class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pointer1 = 0
        pointer2 = len(nums) - 1

        while pointer1 <= pointer2:
            midP = (pointer1 + pointer2) // 2

            if nums[midP] == target:
                return midP
            elif nums[midP] > target:
                pointer2 = midP - 1
            else:
                pointer1 = midP + 1
        
        return pointer1