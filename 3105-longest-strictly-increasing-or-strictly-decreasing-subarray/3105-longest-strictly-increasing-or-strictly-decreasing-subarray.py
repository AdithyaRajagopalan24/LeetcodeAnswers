class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = inc_len = dec_len = 1
        for n1, n2 in pairwise(nums): 
            if n1 < n2: 
                inc_len += 1
                dec_len = 1
            elif n1 > n2:
                dec_len += 1
                inc_len = 1
            else: 
                inc_len = dec_len = 1
            max_len = max(max_len, inc_len, dec_len) 
        return max_len