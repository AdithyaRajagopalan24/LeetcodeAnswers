class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[0:k][::-1] + s[k:]