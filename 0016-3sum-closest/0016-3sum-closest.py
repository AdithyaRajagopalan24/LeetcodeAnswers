class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if abs(currentSum -target) < abs(closestSum - target):
                    closestSum = currentSum
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return currentSum
        
        return closestSum