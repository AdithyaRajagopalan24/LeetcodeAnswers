class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        nums = len(bits)
        i = 0
        while i < nums - 1:
            i += 1 + (bits [i] == 1)
        return (i == nums - 1)