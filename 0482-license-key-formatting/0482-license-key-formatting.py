class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace("-", "").upper()
        firstGroupLen = len(cleaned) % k or k
        parts = [cleaned[:firstGroupLen]]
        i = firstGroupLen
        while i < len(cleaned):
            parts.append(cleaned[i:i+k])
            i += k
        return "-".join(parts)
