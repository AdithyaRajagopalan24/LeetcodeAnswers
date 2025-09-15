class Solution:
    def canBeTypedWords(self, text: str, bl: str) -> int:
        l=list(text.split(" "))
        c=0
        for i in l:
            for j in bl:
                if j in i:
                    break
            else:
                c+=1
        return c