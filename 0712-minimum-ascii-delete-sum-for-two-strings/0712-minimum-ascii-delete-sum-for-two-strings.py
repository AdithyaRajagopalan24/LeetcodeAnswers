class Solution:
    def minimumDeleteSum(self, firstString: str, secondString: str) -> int:
        lengthA, lengthB = len(firstString), len(secondString)
        dp = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]

        for indexA in range(lengthA - 1, -1, -1):
            for indexB in range(lengthB - 1, -1, -1):
                if firstString[indexA] == secondString[indexB]:
                    dp[indexA][indexB] = ord(firstString[indexA]) + dp[indexA + 1][indexB + 1]
                else:
                    dp[indexA][indexB] = max(
                        dp[indexA + 1][indexB],
                        dp[indexA][indexB + 1]
                    )

        totalAsciiSum = sum(ord(char) for char in firstString) + sum(ord(char) for char in secondString)
        return totalAsciiSum - 2 * dp[0][0]
