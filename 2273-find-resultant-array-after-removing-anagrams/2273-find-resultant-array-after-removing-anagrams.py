class Solution(object):
    def removeAnagrams(self, words):
        def isAnagram(s1, s2):
            return sorted(s1) == sorted(s2)
        
        wordsSet = []
        for i in words:
            if wordsSet and isAnagram(wordsSet[-1], i):
                continue
            wordsSet.append(i)
        return wordsSet