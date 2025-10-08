class Solution:
    def successfulPairs(self, spells, potions, success: int):
        potions.sort()
        m = len(potions)
        ans = []
        for spell in spells:
            tar = success // spell
            tar += 0 if success % spell == 0 else 1
            idx = bisect_left(potions, tar)
            ans.append(m - idx)
        return ans