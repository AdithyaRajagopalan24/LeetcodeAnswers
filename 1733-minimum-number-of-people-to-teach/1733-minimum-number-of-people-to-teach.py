from typing import List
from collections import Counter

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(x) for x in languages]
        needTeach = set()
        for a, b in friendships:
            a -= 1
            b -= 1
            if langs[a].isdisjoint(langs[b]):
                needTeach.add(a)
                needTeach.add(b)
        if not needTeach:
            return 0
        langCount = Counter()
        for person in needTeach:
            for lang in langs[person]:
                langCount[lang] += 1
        return len(needTeach) - max(langCount.values(), default=0)
