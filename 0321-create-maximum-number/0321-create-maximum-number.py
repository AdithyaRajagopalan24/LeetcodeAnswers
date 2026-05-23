class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMaxSubsequence(nums: List[int], size: int) -> Deque[int]:
            stack = deque()
            removalsLeft = len(nums) - size
            for digit in nums:
                while removalsLeft and stack and stack[-1] < digit:
                    stack.pop()
                    removalsLeft -= 1
                stack.append(digit)
            while len(stack) > size:
                stack.pop()
            return stack
        bestSequence = []

        for countFromNums1 in range(
            max(0, k - len(nums2)),
            min(len(nums1), k) + 1
        ):
            subsequence1 = getMaxSubsequence(nums1, countFromNums1)
            subsequence2 = getMaxSubsequence(nums2, k - countFromNums1)
            merged = []
            while subsequence1 or subsequence2:
                if subsequence1 > subsequence2:
                    merged.append(subsequence1.popleft())
                else:
                    merged.append(subsequence2.popleft())
            bestSequence = max(bestSequence, merged)
        return bestSequence