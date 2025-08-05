class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefixSum = 0
        countMap = {0: 1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in countMap:
                result += countMap[prefixSum - k]
            countMap[prefixSum] = countMap.get(prefixSum, 0) + 1

        return result
