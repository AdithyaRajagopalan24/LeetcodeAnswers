class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 in seen and i - seen[val1] <= k:
                return True
            else:
                seen[val1] = i
        
        return False