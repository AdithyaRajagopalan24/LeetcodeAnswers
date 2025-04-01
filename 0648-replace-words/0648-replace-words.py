import re
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wordsList = sentence.split(" ")
        finalSentence = ""
        for i in dictionary:
            for j in range(len(wordsList)):
                if wordsList[j].startswith(i):
                    wordsList[j] = i
        for i in wordsList:
            finalSentence = finalSentence + i + " "
        return(finalSentence[:-1:])