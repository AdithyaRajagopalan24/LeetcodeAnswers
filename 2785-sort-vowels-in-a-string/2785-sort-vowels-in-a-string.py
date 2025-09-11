class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = iter(sorted(ch for ch in s if ch in "AEIOUaeiou"))
        return "".join(next(vowels) if ch in "AEIOUaeiou" else ch for ch in s)
