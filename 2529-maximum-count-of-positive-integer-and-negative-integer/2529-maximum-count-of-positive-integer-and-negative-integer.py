class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
        
        if l < n and nums[l] != 0:
            return max(l, n - l)
        
        neg = l
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == 0:
                l = mid + 1
            else:
                r = mid - 1
        
        return max(neg, n - l)