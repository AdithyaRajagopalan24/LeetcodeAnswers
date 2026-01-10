class Solution:
    def reverseWords(self, s: str) -> str:
        wordsList = s.split()
        vowelsSet = set("aeiou")
        vowelCount = sum(1 for ch in wordsList[0] if ch in vowelsSet)

        for index in range(1, len(wordsList)):
            currentCount = sum(1 for ch in wordsList[index] if ch in vowelsSet)
            if currentCount == vowelCount:
                wordsList[index] = wordsList[index][::-1]

        return " ".join(wordsList)
