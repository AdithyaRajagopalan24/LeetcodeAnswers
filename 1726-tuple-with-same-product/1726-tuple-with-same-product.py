class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_count = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        total = 0
        for count in product_count.values():
            if count >= 2:
                total += count * (count - 1) // 2
        
        return total * 8