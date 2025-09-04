from collections import defaultdict

class Solution:
    def minCut(self, inputString: str) -> int:
        palindromeMap = defaultdict(list)
        length = len(inputString)

        for center in range(length):
            left, right = center, center + 1
            while left >= 0 and right <= length and inputString[left] == inputString[right - 1]:
                palindromeMap[right].append(left)
                left -= 1
                right += 1

            left, right = center, center + 2
            while left >= 0 and right <= length and inputString[left] == inputString[right - 1]:
                palindromeMap[right].append(left)
                left -= 1
                right += 1

        minCuts = [i for i in range(-1, length)]
        for endIndex in range(1, length + 1):
            minCuts[endIndex] = min(minCuts[startIndex] for startIndex in palindromeMap[endIndex]) + 1

        return minCuts[-1]
