class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        dup = 0
        for x in nums:
            if x in s:
                dup = x
            s.add(x)
        total = n * (n + 1) // 2
        missing = total - (sum(nums) - dup)
        return [dup, missing]