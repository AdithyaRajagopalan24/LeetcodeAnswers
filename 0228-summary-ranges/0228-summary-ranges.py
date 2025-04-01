class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        break_point = 0
        k = 0
        l = []

        if len(nums) == 1:
            l.append(f"{nums[0]}")

        for i in range(1, len(nums)):
            
            if nums[i] - nums[k] > 1:
                if nums[break_point] == nums[k]:
                    l.append(f"{nums[i - 1]}")
                else:
                    l.append(f"{nums[break_point]}->{nums[k]}")
                break_point = i


            if i == len(nums) - 1:
                if nums[break_point] == nums[i]:
                    l.append(f"{nums[i]}")
                else:
                    l.append(f"{nums[break_point]}->{nums[i]}")

            k += 1

        return l