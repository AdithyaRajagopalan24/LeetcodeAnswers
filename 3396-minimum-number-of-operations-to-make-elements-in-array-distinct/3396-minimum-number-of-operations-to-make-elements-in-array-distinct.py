import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        list2 = []
        for i in nums[::-1]:
            if i in list2:
                return math.ceil(((len(nums) - len(list2))/3))
            else:
                list2.append(i)
        return 0