class Solution:
    def sortPermutation(self, nums):
        bitMask = (1 << 30) - 1
        for index, value in enumerate(nums):
            if value != index:
                bitMask &= value
        return 0 if bitMask == (1 << 30) - 1 else bitMask
