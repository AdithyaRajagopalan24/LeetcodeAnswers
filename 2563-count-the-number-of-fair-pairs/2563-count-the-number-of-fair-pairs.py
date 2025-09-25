from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def countpairswith_sum_at_most(target: int) -> int:
            count = 0
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count
        
        return countpairswith_sum_at_most(upper) - countpairswith_sum_at_most(lower - 1)
