class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for number in nums:
            if number == 2:
                result.append(-1)
                continue
            for bitIndex in range(32):
                if number & (1 << bitIndex) == 0:
                    updatedValue = number & ~(1 << (bitIndex - 1))
                    result.append(updatedValue)
                    break

        return result
