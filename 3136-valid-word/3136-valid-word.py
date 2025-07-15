class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        v = c = 0

        for ch in word:
            if ch.isdigit():
                continue
            if ch.isalpha():
                (v := v + 1) if ch in vowels else (c := c + 1)
            else:
                return False
        return v > 0 and c > 0