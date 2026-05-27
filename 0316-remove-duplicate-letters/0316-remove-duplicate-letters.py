class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remain = Counter(s)
        stack = []
        seen = set()

        for ch in s:
            remain[ch] -= 1
            if ch in seen:
                continue

            while stack and stack[-1] > ch and remain[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)