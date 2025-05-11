class Solution:
    def threeConsecutiveOdds(self, a):
        total = 0
        for x in a:
            total = total + 1 if x % 2 else 0
            if total == 3:
                return True
        return False