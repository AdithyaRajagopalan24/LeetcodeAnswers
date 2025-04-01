class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = sorted(s, reverse=True)
        result = []
        freq = 1
        indexPointer = 0
        for i in range(len(chars)):
            if result and result[-1] == chars[i]:
                if freq < repeatLimit:
                    result.append(chars[i])
                    freq += 1
                else:
                    indexPointer = max(indexPointer, i + 1)
                    while indexPointer < len(chars) and chars[indexPointer] == chars[i]:
                        indexPointer += 1
                    if indexPointer < len(chars):
                        result.append(chars[indexPointer])
                        chars[i], chars[indexPointer] = chars[indexPointer], chars[i]
                        freq = 1
                    else:
                        break
            else:
                result.append(chars[i])
                freq = 1
        return ''.join(result)