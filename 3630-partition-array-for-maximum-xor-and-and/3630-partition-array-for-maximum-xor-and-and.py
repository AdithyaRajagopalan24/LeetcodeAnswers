class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for mask in range(1 << n):
            s = 0
            bVal = None
            candidates = []
            for i in range(n):
                if (1 << i) & mask:
                    if bVal is None:
                        bVal = nums[i]
                    else:
                        bVal &= nums[i]
                else:
                    s ^= nums[i]
                    candidates.append(nums[i])

            filtered = [x & ~s for x in candidates]
            basis = []
            for x in filtered:
                for b in basis:
                    x = min(x, x ^ b)
                if x:
                    basis.append(x)

            basis.sort(reverse=True)
            xMax = 0
            for b in basis:
                xMax = max(xMax, xMax ^ b)

            bVal = 0 if bVal is None else bVal
            res = max(res, bVal + s + ((~s & xMax) << 1))
        return res
