import numpy as np

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        digitArray = np.frombuffer(s.encode('ascii'), dtype=np.uint8) - ord('0')

        prefixCount = np.empty((5, n), dtype=np.int64)
        for digit in range(5):
            isDigit = (digitArray == digit).astype(np.int64)
            prefixCount[digit] = np.cumsum(isDigit)

        closestRightIndex = np.full((5, n), n, dtype=np.int64)
        for digit in range(5):
            positions = np.flatnonzero(digitArray == digit)
            if positions.size:
                posIndex = np.searchsorted(positions, np.arange(n))
                valid = posIndex < positions.size
                closestRightIndex[digit, valid] = positions[posIndex[valid]]

        maxDiff = -10**9

        for oddDigit in range(5):
            for evenDigit in range(5):
                if oddDigit == evenDigit:
                    continue

                oddPrefix = prefixCount[oddDigit]
                evenPrefix = prefixCount[evenDigit]

                oddParity = (oddPrefix % 2).astype(np.int64)
                evenParity = (evenPrefix % 2).astype(np.int64)

                suffixMax = np.full((2, 2, n), -10**9, dtype=np.int64)

                validMask = (oddPrefix > 0) & (evenPrefix > 0)
                diffArray = oddPrefix - evenPrefix
                validIndices = np.where(validMask)[0]

                suffixMax[oddParity[validIndices], evenParity[validIndices], validIndices] = diffArray[validIndices]

                for op in (0, 1):
                    for ep in (0, 1):
                        suffixMax[op, ep] = np.maximum.accumulate(suffixMax[op, ep][::-1])[::-1]

                startCount = n - k + 1
                startIndices = np.arange(startCount, dtype=np.int64)

                oddBefore = np.where(startIndices == 0, 0, oddPrefix[startIndices - 1])
                evenBefore = np.where(startIndices == 0, 0, evenPrefix[startIndices - 1])

                targetOddParity = (oddBefore + 1) % 2
                targetEvenParity = evenBefore % 2

                endIndex = startIndices + k - 1
                nextOdd = closestRightIndex[oddDigit, startIndices]
                nextEven = closestRightIndex[evenDigit, startIndices]
                queryIndices = np.maximum.reduce([endIndex, nextOdd, nextEven])

                validQuery = queryIndices < n
                candidateDiffs = -10**9 * np.ones(startCount, dtype=np.int64)

                for op in (0, 1):
                    for ep in (0, 1):
                        mask = (targetOddParity == op) & (targetEvenParity == ep) & validQuery
                        if np.any(mask):
                            candidateDiffs[mask] = np.maximum(candidateDiffs[mask],
                                                              suffixMax[op, ep][queryIndices[mask]] - 
                                                              oddBefore[mask] + evenBefore[mask])

                maxDiff = max(maxDiff, candidateDiffs.max())

        return int(maxDiff)
