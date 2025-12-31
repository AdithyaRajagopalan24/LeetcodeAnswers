from collections import defaultdict

class Solution:
    def minSwaps(self, nums, forbidden):
        n = len(nums)
        countMap = defaultdict(int)
        
        for num in nums:
            countMap[num] += 1
        
        for num in forbidden:
            countMap[num] += 1
        
        for count in countMap.values():
            if count > n:
                return -1
        
        forbiddenCountMap = defaultdict(int)
        totalMatches = 0
        
        for i in range(n):
            if nums[i] == forbidden[i]:
                forbiddenCountMap[nums[i]] += 1
                totalMatches += 1
        
        if totalMatches == 0:
            return 0
        
        maxSwaps = 0
        for count in forbiddenCountMap.values():
            maxSwaps = max(maxSwaps, count)
        
        return max(maxSwaps, (totalMatches + 1) // 2)
