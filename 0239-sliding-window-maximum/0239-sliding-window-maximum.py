from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        dq = deque()

        for i in range(len(nums)):
            while dq and dq[-1] < nums[i]:
                dq.pop()

            dq.append(nums[i])

            if i >= k and nums[i - k] == dq[0]:
                dq.popleft()

            if i >= k - 1:
                ans.append(dq[0])

        return ans