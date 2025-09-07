class Solution:
    def shortestPalindrome(self, text: str) -> str:
        matchCount, length = 0, len(text)
        for char in text[::-1]:
            if char == text[matchCount]:
                matchCount += 1
        if matchCount == length:
            return text
        suffix = text[matchCount:]
        return suffix[::-1] + self.shortestPalindrome(text[:matchCount]) + suffix
