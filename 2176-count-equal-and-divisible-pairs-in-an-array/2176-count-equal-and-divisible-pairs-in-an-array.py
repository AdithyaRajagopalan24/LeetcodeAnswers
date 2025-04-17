class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if nums == list(set(nums)) and k > (n-1)*(n-2):
            return 0
        pos = defaultdict(list)
        count = 0
        for i, val in enumerate(nums):
            for j in pos[val]:
                if (i * j) % k == 0:
                    count += 1
            pos[val].append(i)
        return count