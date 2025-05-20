class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n, m=len(nums), len(queries)
        freq=[0]*(n+1)
        for s, e in queries:
            freq[s]+=1
            freq[e+1]-=1
        netVal=0
        for i, x in enumerate(nums):
            netVal+=freq[i]
            if x>netVal: return False
        return True