class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneDict = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def checkAgain(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            possible_letters = phoneDict[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                checkAgain(index + 1, path)
                path.pop()  # checkAgain
        combinations = []
        checkAgain(0, [])
        return combinations