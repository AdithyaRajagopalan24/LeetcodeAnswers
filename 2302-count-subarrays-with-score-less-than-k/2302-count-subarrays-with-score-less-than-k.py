class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        N=len(nums)
        l=0
        cur=0
        for r in range(N):
            cur+=nums[r]
            if cur*(r-l+1)>=k:
                while cur*(r-l+1)>=k and l<=r:
                    cur-=nums[l]
                    l+=1
            cur_len=r-l+1
            res+=cur_len
        
        return res