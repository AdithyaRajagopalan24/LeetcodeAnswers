class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        count = [0] * (max(fruits) + 1)
        maxLen, currLen, types, left = 0, 0, 0, 0
        for right, fruit in enumerate(fruits):
            count[fruit] += 1
            if count[fruit] == 1:
                types += 1
            currLen += 1
            while types > 2:
                drop = fruits[left]
                count[drop] -= 1
                if count[drop] == 0:
                    types -= 1
                left += 1
                currLen -= 1
            maxLen = max(maxLen, currLen)
        return maxLen
