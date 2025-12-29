class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        index = length - 1
        seen = {}
        
        if length % 3 != 0:
            if length % 3 == 1:
                seen[nums[index]] = 1
                index -= 1
            if length % 3 == 2:
                seen[nums[index]] = 1
                if nums[index] == nums[index - 1]: 
                    return length // 3 + 1
                else: 
                    seen[nums[index - 1]] = 1
                index -= 2
        
        while index >= 0:
            if nums[index] in seen: 
                return index // 3 + 1
            else: 
                seen[nums[index]] = 1
            index -= 1
        
        return 0