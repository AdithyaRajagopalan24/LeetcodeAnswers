from collections import Counter


class SqrtDecomposition:
    def __init__(self, nums):
        n = len(nums)
        blockSize = int(n ** 0.5) + 1

        blockFreq = [Counter() for _ in range(blockSize)]
        lazy = [0] * blockSize

        for i, value in enumerate(nums):
            blockFreq[i // blockSize][value] += 1

        self.n = n
        self.blockSize = blockSize
        self.nums = list(nums)
        self.blockFreq = blockFreq
        self.lazy = lazy

    def add(self, left, right, increment):
        i = left

        while i <= right:
            block = i // self.blockSize

            if i % self.blockSize == 0 and i + self.blockSize - 1 <= right:
                self.lazy[block] += increment
                i += self.blockSize
            else:
                oldValue = self.nums[i]
                newValue = oldValue + increment

                self.blockFreq[block][oldValue] -= 1
                if self.blockFreq[block][oldValue] == 0:
                    del self.blockFreq[block][oldValue]

                self.blockFreq[block][newValue] += 1
                self.nums[i] = newValue
                i += 1

    def count(self, value):
        total = 0

        for block in range(len(self.blockFreq)):
            total += self.blockFreq[block][value - self.lazy[block]]

        return total


class Solution:
    def numberOfPairs(self, nums1, nums2, queries):
        sqrt = SqrtDecomposition(nums2)
        answer = []

        for query in queries:
            if query[0] == 1:
                sqrt.add(query[1], query[2], query[3])
            else:
                pairs = 0

                for value in nums1:
                    pairs += sqrt.count(query[1] - value)

                answer.append(pairs)

        return answer