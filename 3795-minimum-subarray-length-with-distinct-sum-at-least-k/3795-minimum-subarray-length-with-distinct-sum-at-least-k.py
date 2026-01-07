from collections import defaultdict

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        minLength = float('inf')
        freq = defaultdict(int)
        leftPointer = 0
        distinctSum = 0
        for rightPointer in range(len(nums)):
            if nums[rightPointer] not in freq or freq[nums[rightPointer]] == 0:
                distinctSum += nums[rightPointer]
            freq[nums[rightPointer]] += 1

            while distinctSum >= k:
                currentLength = rightPointer - leftPointer + 1
                minLength = min(currentLength, minLength)
                
                freq[nums[leftPointer]] -= 1
                if freq[nums[leftPointer]] == 0:
                    distinctSum -= nums[leftPointer]
                leftPointer += 1
        
        return minLength if minLength != float('inf') else -1
