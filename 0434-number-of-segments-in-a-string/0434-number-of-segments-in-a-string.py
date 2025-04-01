class Solution:
    def countSegments(self, s: str) -> int:
        s = s.lstrip()
        s = s.rstrip()
        replaceString = re.sub(' +', ' ', s)
        s = replaceString
        if s == "" or s.isspace() == True:
            return 0
        listOfSegments = s.split(" ")
        return len(listOfSegments)