class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        finalList = []
        for i in range(len(words) - 1, -1, -1):
            finalList.append(words[i])
            if i != 0:
                finalList.append(" ")
        return "".join(finalList)