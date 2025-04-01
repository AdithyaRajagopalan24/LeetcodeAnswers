class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        lt, gt = 0, n-1
        i = 0
        
        while i < n:
            if nums[i] > pivot:
                nums.append(nums[i])
                nums.pop(i)
                gt -= 1
                i -= 1
            elif nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
            if i == gt:
                break
            i += 1
        return nums
