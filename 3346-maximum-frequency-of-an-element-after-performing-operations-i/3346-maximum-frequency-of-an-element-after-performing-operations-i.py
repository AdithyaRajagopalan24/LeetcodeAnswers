class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOps: int) -> int:
        maxVal = max(nums)
        size = maxVal + k + 2
        freq = [0] * size
        for num in nums:
            freq[num] += 1

        prefixSum = [0] * size
        prefixSum[0] = freq[0]
        for i in range(1, size):
            prefixSum[i] = prefixSum[i - 1] + freq[i]

        maxFreq = 0
        for target in range(size):
            if freq[target] == 0 and numOps == 0:
                continue
            left = max(0, target - k)
            right = min(size - 1, target + k)
            total = prefixSum[right] - (prefixSum[left - 1] if left > 0 else 0)
            adjustable = total - freq[target]
            possible = freq[target] + min(numOps, adjustable)
            maxFreq = max(maxFreq, possible)

        return maxFreq
