class Solution:
    def totalMoney(self, n: int) -> int:
        w, d = divmod(n,7)
        return (w * (49 + 7 * w) + d * (2*w + d + 1)) // 2