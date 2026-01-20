class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        finalVal = []

        for i in nums:
            found = -1
            for j in range(i + 1):
                if (j | (j + 1)) == i:
                    found = j
                    break
            finalVal.append(found)

        return finalVal