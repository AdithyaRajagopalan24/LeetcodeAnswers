class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for char1 in s:
            if char1 in "aeiou":
                return True
        return False