from collections import Counter
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        candidateSet = set()
        for num in nums:
            candidateSet.add(num - k)
            candidateSet.add(num)
            candidateSet.add(num + k)
        candidates = sorted(candidateSet)
        m = len(candidates)
        diffArray = [0] * (m + 1)
        for num in nums:
            leftIndex = bisect_left(candidates, num - k)
            rightIndex = bisect_right(candidates, num + k) - 1
            if leftIndex <= rightIndex:
                diffArray[leftIndex] += 1
                diffArray[rightIndex + 1] -= 1
        freqCount = Counter(nums)
        result = 0
        currCount = 0
        for i, val in enumerate(candidates):
            currCount += diffArray[i]
            equalCount = freqCount.get(val, 0)
            result = max(result, equalCount + min(numOperations, currCount - equalCount))
        return result
