class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        indices = []
        for i in range(len(nums)):
            curVal = 0
            for j in range(i + 1, len(nums)):
                if nums[i] % 2 != 0 and nums[j] % 2== 0 or nums[i] % 2 == 0 and nums[j] % 2 != 0:
                    curVal += 1
            indices.append(curVal)
        return indices