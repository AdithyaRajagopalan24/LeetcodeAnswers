from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countPairsLessEqual(targetProduct):
            totalCount = 0
            numNegativesInNums1 = sum(1 for num in nums1 if num < 0)

            rowStart = numNegativesInNums1 - 1 if targetProduct >= 0 else 0
            rowEnd = -1 if targetProduct >= 0 else numNegativesInNums1
            rowStep = -1 if targetProduct >= 0 else 1
            colPointer = 0

            # Count pairs with negative numbers in nums1
            for i in range(rowStart, rowEnd, rowStep):
                while colPointer < len(nums2) and nums1[i] * nums2[colPointer] > targetProduct:
                    colPointer += 1
                totalCount += len(nums2) - colPointer

            rowStart = numNegativesInNums1 if targetProduct >= 0 else len(nums1) - 1
            rowEnd = len(nums1) if targetProduct >= 0 else numNegativesInNums1 - 1
            rowStep = 1 if targetProduct >= 0 else -1
            colPointer = len(nums2) - 1

            # Count pairs with non-negative numbers in nums1
            for i in range(rowStart, rowEnd, rowStep):
                if nums1[i] == 0:
                    if targetProduct >= 0:
                        totalCount += len(nums2)
                    continue
                while colPointer >= 0 and nums1[i] * nums2[colPointer] > targetProduct:
                    colPointer -= 1
                totalCount += colPointer + 1

            return totalCount

        leftBound, rightBound = -10**10, 10**10
        while leftBound <= rightBound:
            midProduct = (leftBound + rightBound) // 2
            if countPairsLessEqual(midProduct) >= k:
                rightBound = midProduct - 1
            else:
                leftBound = midProduct + 1

        return leftBound
