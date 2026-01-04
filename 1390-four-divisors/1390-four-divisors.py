class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        totalSum = 0

        for num in nums:
            divisorCount = 0
            divisorSum = 0

            divisor = 1
            while divisor * divisor <= num:
                if num % divisor == 0:
                    otherDivisor = num // divisor

                    divisorCount += 1
                    divisorSum += divisor

                    if otherDivisor != divisor:
                        divisorCount += 1
                        divisorSum += otherDivisor

                    if divisorCount > 4:
                        break
                divisor += 1

            if divisorCount == 4:
                totalSum += divisorSum

        return totalSum
