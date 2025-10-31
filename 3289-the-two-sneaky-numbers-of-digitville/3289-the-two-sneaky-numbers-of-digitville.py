from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        maxVal = max(nums)
        countArr = [0] * (maxVal + 1)
        result = []
        for num in nums:
            countArr[num] += 1
        for i in range(len(countArr)):
            if countArr[i] == 2:
                result.append(i)
        return result