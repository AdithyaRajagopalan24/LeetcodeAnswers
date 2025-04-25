class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        res = 0
        count = {0: 1}
        current_count = 0
        n = len(nums)

        for num in nums:
            if num % modulo == k:
                current_count += 1
            target = (current_count - k) % modulo
            if target in count:
                res += count[target]
            if current_count % modulo in count:
                count[current_count % modulo] += 1
            else:
                count[current_count % modulo] = 1

        return res
