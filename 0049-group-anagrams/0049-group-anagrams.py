import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)

        return list(anagram_map.values())
