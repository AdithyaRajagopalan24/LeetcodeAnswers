class Solution:
    def minOperations(self, nums):
        cnt = 0
        for i in range(len(nums) - 2):
            if nums[i] == 1:
                continue
            else:
                cnt += 1
            for j in range(i, i + 3):
                nums[j] = 0 if nums[j] == 1 else 1
        if any(num == 0 for num in nums):
            return -1
        return cnt
