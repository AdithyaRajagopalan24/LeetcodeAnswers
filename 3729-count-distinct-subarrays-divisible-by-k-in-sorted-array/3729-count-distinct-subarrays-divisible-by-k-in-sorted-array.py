class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        nums.append(0)
        remainderCount = defaultdict(int)
        remainderCount[0] = 1
        result = 0
        index = 0
        repeatCount = 1
        currentSum = 0
        
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                repeatCount += 1
            else:
                value = nums[index]
                prevSum = currentSum
                for _ in range(repeatCount):
                    currentSum += value
                    if currentSum < k:
                        continue
                    remainder = currentSum % k
                    result += remainderCount[remainder]
                for _ in range(repeatCount):
                    prevSum += value
                    remainderCount[prevSum % k] += 1
                repeatCount = 1
            index += 1
        return result
