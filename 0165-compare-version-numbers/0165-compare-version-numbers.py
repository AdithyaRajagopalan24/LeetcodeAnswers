class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")
        i = 0
        while i < len(parts1) or i < len(parts2):
            v1 = int(parts1[i]) if i < len(parts1) else 0
            v2 = int(parts2[i]) if i < len(parts2) else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            i += 1
        return 0


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")
        maxLen = max(len(parts1), len(parts2))
        for i in range(maxLen):
            v1 = int(parts1[i]) if i < len(parts1) else 0
            v2 = int(parts2[i]) if i < len(parts2) else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0
