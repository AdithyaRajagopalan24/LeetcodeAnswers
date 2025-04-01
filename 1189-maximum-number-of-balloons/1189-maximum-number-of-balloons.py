class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charsDict = {i: text.count(i) for i in "balloon"}
        charsDict['l'] = charsDict['l'] // 2
        charsDict['o'] = charsDict['o'] // 2
        return min(charsDict.values())