class Solution:
    def findMaxVal(self, n, restrictions, diff):
        leftLimit = [10**6] * n
        rightLimit = [10**6] * n
        upperBound = [10**6] * n

        for restriction in restrictions:
            index = restriction[0]
            maxValue = restriction[1]
            leftLimit[index] = maxValue
            rightLimit[index] = maxValue
            upperBound[index] = maxValue

        leftLimit[0] = 0
        rightLimit[0] = 0
        upperBound[0] = 0

        for i in range(n - 1):
            leftLimit[i + 1] = min(leftLimit[i] + diff[i], leftLimit[i + 1])

        for i in range(n - 2, -1, -1):
            rightLimit[i] = min(rightLimit[i + 1] + diff[i], rightLimit[i])

        for i in range(n):
            upperBound[i] = min(leftLimit[i], rightLimit[i])

        maxResult = 0
        for value in upperBound:
            maxResult = max(maxResult, value)

        return maxResult
