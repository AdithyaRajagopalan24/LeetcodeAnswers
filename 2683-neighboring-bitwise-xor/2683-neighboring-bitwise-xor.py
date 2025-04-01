class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for i in derived:
            ans ^= i
        return False if ans else True