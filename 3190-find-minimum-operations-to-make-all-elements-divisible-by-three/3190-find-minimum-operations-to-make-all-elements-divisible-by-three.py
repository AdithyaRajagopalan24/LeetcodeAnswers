class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opCount=0
        for i in nums:
            if i%3!=0:
                opCount+=1
        return opCount