from typing import List

class Solution:
    def isVowel(self, c: str) -> bool:
        return c in "aeiou"

    def maskVowels(self, s: str) -> str:
        return ''.join('a' if ch in "aeiou" else ch for ch in s)

    def spellchecker(self, wordList: List[str], queries: List[str]) -> List[str]:
        exactWords = set(wordList)
        lowerMap = {}
        vowelMap = {}

        for word in wordList:
            lowerWord = word.lower()
            lowerMap.setdefault(lowerWord, word)
            maskedWord = self.maskVowels(lowerWord)
            vowelMap.setdefault(maskedWord, word)

        result = []
        for query in queries:
            if query in exactWords:
                result.append(query)
                continue
            lowerQuery = query.lower()
            if lowerQuery in lowerMap:
                result.append(lowerMap[lowerQuery])
                continue
            maskedQuery = self.maskVowels(lowerQuery)
            result.append(vowelMap.get(maskedQuery, ""))
        return result
