from collections import defaultdict, deque


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        n = len(nums)

        ans = 0
        highestBit = max(nums).bit_length() - 1

        for bit in range(highestBit, -1, -1):
            candidate = ans | (1 << bit)

            prefixXor = 0
            left = 0

            minDeque = deque()
            maxDeque = deque()

            prefixPos = defaultdict()
            prefixPos[0] = -1

            for right in range(n):
                curNum = nums[right]

                prefixXor ^= (curNum & candidate)

                while minDeque and curNum <= nums[minDeque[-1]]:
                    minDeque.pop()

                while maxDeque and curNum >= nums[maxDeque[-1]]:
                    maxDeque.pop()

                minDeque.append(right)
                maxDeque.append(right)

                while nums[maxDeque[0]] - nums[minDeque[0]] > k:
                    if minDeque[0] == left:
                        minDeque.popleft()

                    if maxDeque[0] == left:
                        maxDeque.popleft()

                    left += 1

                needed = candidate ^ prefixXor

                if needed in prefixPos and prefixPos[needed] >= left - 1:
                    ans = candidate
                    break

                prefixPos[prefixXor] = right

        return ans