class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total

        firstRemainder = list()
        secondRemainder = list()
        for n in nums:
            if n % 3 == 1:
                firstRemainder.append(n)
            elif n % 3 == 2:
                secondRemainder.append(n)
        
        firstRemainder.sort()
        secondRemainder.sort()
        
        possibleAnswers = [0]
        if total % 3 == 1:
            if firstRemainder:
                possibleAnswers.append(total - firstRemainder[0])
            if len(secondRemainder) >= 2:
                possibleAnswers.append(total - secondRemainder[0] - secondRemainder[1])
        else:
            if secondRemainder:
                possibleAnswers.append(total - secondRemainder[0])
            if len(firstRemainder) >= 2:
                possibleAnswers.append(total - firstRemainder[0] - firstRemainder[1])
        
        return max(possibleAnswers)