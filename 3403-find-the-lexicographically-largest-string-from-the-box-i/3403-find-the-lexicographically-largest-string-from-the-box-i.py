class Solution:
    def answerString(self, word: str, nf: int) -> str:
        if nf == 1:
            return word
        n = len(word)

        checkedString = ''
        highestChar= 'a'
        for i in range(n):
            if word[i] >= highestChar:
                splits_left = (nf-i) if (nf-i)>=0 else 0
                checkedString = max(checkedString, word[i:n-splits_left+1])
                highestChar = word[i]
            
        return checkedString