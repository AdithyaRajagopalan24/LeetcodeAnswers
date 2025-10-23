class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], cap: int) -> List[bool]:
        nums.sort()
        canSum = [False] * (cap + 1)
        canSum[0] = True
        result, idx, n = [], 0, len(nums)
        
        for limit in range(1, n + 1):
            while idx < n and nums[idx] <= limit:
                for s in range(cap, nums[idx] - 1, -1):
                    if canSum[s - nums[idx]]:
                        canSum[s] = True
                idx += 1
            result.append(any(canSum[s] for s in range(cap, max(0, cap - limit * (n - idx)) - 1, -limit)))
        
        return result
