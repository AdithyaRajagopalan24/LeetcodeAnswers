class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos1 = 1
        for pos2 in range(1, len(nums)):
            if nums[pos2] != nums[pos2 - 1]:
                nums[pos1] = nums[pos2]
                pos1 += 1
        return pos1