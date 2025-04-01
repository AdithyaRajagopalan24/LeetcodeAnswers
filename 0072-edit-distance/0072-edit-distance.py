class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)
        previous = [j for j in range(length2 + 1)]
        current = [0] * (length2 + 1)
        for i in range(1, length1 + 1):
            current[0] = i
            for j in range(1, length2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    current[j] = previous[j - 1]
                else:
                    insertion = 1 + current[j - 1]
                    deletion = 1 + previous[j]
                    replacement = 1 + previous[j - 1]
                    current[j] = min(insertion, deletion, replacement)
            previous = current[:]
        return previous[length2]