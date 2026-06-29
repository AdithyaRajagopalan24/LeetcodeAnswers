class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        allCombinations = []
        phoneDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def check(index, path):
            if index == len(digits):
                allCombinations.append("".join(path))
                return
            
            letterOptions = phoneDict[digits[index]]

            for curLetter in letterOptions:
                path.append(curLetter)
                check(index + 1, path)
                path.pop()
        
        check(0, [])
        return allCombinations