class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            count = 0
            for y in nums:
                if y < x:
                    count += 1
            res.append(count)
        return res