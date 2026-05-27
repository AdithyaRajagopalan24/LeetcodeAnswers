class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lisTails = []
        for num in nums:
            insertPos = bisect_left(lisTails, num)
            if insertPos == 2:
                return True
            if insertPos == len(lisTails):
                lisTails.append(num)
            else:
                lisTails[insertPos] = num
        return False