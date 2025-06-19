class Solution:
    def countingSort(self, nums):
        arr = [0] * 100001
        for num in nums:
            arr[num] += 1
        x = 0
        for i in range(len(arr)):
            while arr[i] > 0:
                nums[x] = i
                arr[i] -= 1
                x += 1
    
    def partitionArray(self, nums, k):
        if len(nums) == 1:
            return 1
        self.countingSort(nums)
        part = 1
        i = 0
        a = nums[i]
        while i < len(nums):
            if nums[i] - a <= k:
                i += 1
            else:
                part += 1
                a = nums[i]
        return part