class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums1 = set(nums)
        dict = {}
        for num in nums1:
            dict[num] = 0
        for i in range(len(nums)):
            dict[nums[i]] += 1
        result = sorted(dict, key=dict.get, reverse=True)[:k]
        return result