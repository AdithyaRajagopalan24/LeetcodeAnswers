class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        mod = 0
        for bit in nums:
            mod = (mod * 2 + bit) % 5
            answer.append(mod == 0)
        return answer