class Solution:
    def minMoves(self, arr):
        if sum(arr) < 0:
            return -1

        n = len(arr)
        deficitIndex = -1

        for i in range(n):
            if arr[i] < 0:
                deficitIndex = i

        if deficitIndex == -1:
            return 0

        totalMoves = 0
        leftPtr = deficitIndex - 1
        rightPtr = deficitIndex + 1

        while arr[deficitIndex] < 0:
            if (rightPtr - deficitIndex) < (deficitIndex - leftPtr):
                rightIndex = rightPtr % n
                transfer = min(abs(arr[deficitIndex]), arr[rightIndex])

                totalMoves += (rightPtr - deficitIndex) * transfer
                arr[deficitIndex] += transfer
                arr[rightIndex] -= transfer

                rightPtr += 1
            else:
                leftIndex = (leftPtr + n) % n
                transfer = min(abs(arr[deficitIndex]), arr[leftIndex])

                totalMoves += (deficitIndex - leftPtr) * transfer
                arr[deficitIndex] += transfer
                arr[leftIndex] -= transfer

                leftPtr -= 1

        return totalMoves
