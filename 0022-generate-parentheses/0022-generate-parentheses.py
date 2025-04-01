class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def checkAgain(current, opens, closes):
            if opens == n and closes == n:
                result.append(current)
                return
            if opens < n:
                checkAgain(current + '(', opens + 1, closes)
            if closes < opens:
                checkAgain(current + ')', opens, closes + 1)
        checkAgain("", 0, 0)
        return result