class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        sortedString = sorted(s)

        if list(s) == sortedString:
            return 0

        prefixSorted = list(s)
        suffixSorted = list(s)

        prefixSorted[:n - 1] = sorted(prefixSorted[:n - 1])
        suffixSorted[1:] = sorted(suffixSorted[1:])

        if prefixSorted == sorted(prefixSorted) or suffixSorted == sorted(suffixSorted):
            return 1

        if prefixSorted[-1] >= prefixSorted[0]:
            return 2

        if suffixSorted[0] <= suffixSorted[-1]:
            return 2

        return 3 if n > 2 else -1