class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = arr
        nums.sort()

        minDiff = float('inf')
        pairs = []

        for i in range(1, len(nums)):
            minDiff = min(minDiff, nums[i] - nums[i - 1])

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == minDiff:
                pairs.append([nums[i - 1], nums[i]])

        return pairs
