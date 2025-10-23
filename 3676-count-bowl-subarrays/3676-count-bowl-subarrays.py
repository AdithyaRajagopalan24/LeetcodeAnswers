class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        bowlStack = []
        ans = 0
        for i in range(len(nums)):
            while bowlStack and nums[bowlStack[-1]]<nums[i]:
                bowlStack.pop()
                if bowlStack and i - bowlStack[0] >=2:
                    ans+=1
            bowlStack.append(i)
        return ans
