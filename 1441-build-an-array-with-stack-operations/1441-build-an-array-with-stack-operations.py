class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        cur = 1
        i = 0
        while i < len(target):
            ops.append("Push")
            if cur == target[i]:
                i += 1
            else:
                ops.append("Pop")
            cur += 1
        return ops