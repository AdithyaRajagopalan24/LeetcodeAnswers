class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        nums = [(i - a,a) for i,a in enumerate(nums) if i>=a]
        nums.sort()
        a = []
        for _, n in nums:
            if len(a) == 0 or a[-1] < n:
                a.append(n)
            else:
                i = bisect.bisect_left(a, n)
                a[i] = n
        
        return len(a)