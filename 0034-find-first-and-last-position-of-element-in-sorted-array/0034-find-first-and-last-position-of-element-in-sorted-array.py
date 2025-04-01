class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                last = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [first, last]