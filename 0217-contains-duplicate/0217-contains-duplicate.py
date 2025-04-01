class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if nums == list(set(nums)):
        #     return False
        # else:
        #     return True


        # dict1 = {}
        # for i in nums:
        #     if i in list(dict1.keys()):
        #         return True
        #     else:
        #         dict1[i] = 1
        # return False

        setOfNums = set()
        for n in nums:
            if n in setOfNums:
                return True
            setOfNums.add(n)
        
        return False