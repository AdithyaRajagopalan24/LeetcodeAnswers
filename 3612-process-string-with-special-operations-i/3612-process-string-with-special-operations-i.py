class Solution:
    def processStr(self, s: str) -> str:
        r=""
        for i in s:
            if i=='*' and len(r)>=1:
                r=r[:-1] 
            elif i=='%':
                r=r[::-1]
            elif i.isalpha():
                r+=i 
            else:
                r+=r 
        return r
            