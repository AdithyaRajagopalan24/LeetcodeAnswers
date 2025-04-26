class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        total = 0
        lastBad = last_min = lastBiggest = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                lastBad = i
            if num == minK:
                last_min = i
            if num == maxK:
                lastBiggest = i

            validStarts = min(last_min, lastBiggest)
            total += max(0, validStarts - lastBad)

        return total