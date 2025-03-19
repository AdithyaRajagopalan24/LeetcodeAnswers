class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        x = re.search(needle, haystack)
        if x == None:
            return -1
        else:
            return x.start()