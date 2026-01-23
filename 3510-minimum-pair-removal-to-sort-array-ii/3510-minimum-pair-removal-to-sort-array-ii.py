from typing import List
from itertools import pairwise
from heapq import heapify, heappop, heappush
from math import inf

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        length = len(nums)
        nums.append(inf)

        prev = [-1] * (length + 1)
        next = [i + 1 for i in range(length + 1)]
        for i in range(1, length + 1):
            prev[i] = i - 1

        minHeap = [(a + b, i) for i, (a, b) in enumerate(pairwise(nums))]
        heapify(minHeap)

        inversions = sum(1 for a, b in pairwise(nums) if a > b)
        operations = 0

        while inversions > 0:
            pairSum, index = heappop(minHeap)
            rightIndex = next[index]

            if rightIndex == -1 or nums[index] + nums[rightIndex] != pairSum or prev[rightIndex] != index:
                continue

            nextIndex = next[rightIndex]

            if prev[index] != -1 and nums[prev[index]] > nums[index]:
                inversions -= 1
            if nums[index] > nums[rightIndex]:
                inversions -= 1
            if nextIndex != -1 and nums[rightIndex] > nums[nextIndex]:
                inversions -= 1

            nums[index] = pairSum
            next[index] = nextIndex
            if nextIndex != -1:
                prev[nextIndex] = index

            if prev[index] != -1 and nums[prev[index]] > nums[index]:
                inversions += 1
            if nextIndex != -1 and nums[index] > nums[nextIndex]:
                inversions += 1

            if prev[index] != -1:
                heappush(minHeap, (nums[prev[index]] + nums[index], prev[index]))
            if nextIndex != -1:
                heappush(minHeap, (nums[index] + nums[nextIndex], index))

            operations += 1

        return operations
