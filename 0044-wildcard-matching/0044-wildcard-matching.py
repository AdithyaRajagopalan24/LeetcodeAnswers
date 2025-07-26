from functools import cache

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        @cache
        def match(textIdx, patternIdx):
            if textIdx < 0 and patternIdx < 0:
                return True
            if patternIdx < 0:
                return False
            if textIdx < 0:
                for idx in range(patternIdx + 1):
                    if pattern[idx] != '*':
                        return False
                return True
            if text[textIdx] == pattern[patternIdx] or pattern[patternIdx] == '?':
                return match(textIdx - 1, patternIdx - 1)
            if pattern[patternIdx] == '*':
                return match(textIdx - 1, patternIdx) or match(textIdx, patternIdx - 1)
            return False
        return match(len(text) - 1, len(pattern) - 1)