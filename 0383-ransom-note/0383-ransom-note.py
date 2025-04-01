class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        valSet = {}
        for i in magazine:
            valSet[i] = 1 + valSet.get(i, 0)
        for i in ransomNote:
            if i not in valSet or valSet[i] <= 0:
                return False
            valSet[i] -= 1
        return True