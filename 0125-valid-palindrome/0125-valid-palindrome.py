class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "";
        s = s.upper()
        if s=="":
            return true
        for i in s:
            if i.isalnum():
                s1 += i
        if s1 == s1[::-1]:
            return True
        else:
            return False