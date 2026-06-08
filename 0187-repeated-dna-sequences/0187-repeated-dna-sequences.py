class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(0, len(s)-9):
            substring = s[i : i + 10]

            if substring in seen:
                repeated.add(substring)

            seen.add(substring)

        return list(repeated)