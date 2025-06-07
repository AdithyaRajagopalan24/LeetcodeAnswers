import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        activeCharHeap = []
        charIndexStacks = [[] for _ in range(26)]

        for index, char in enumerate(s):
            if char == "*":
                while activeCharHeap and not charIndexStacks[activeCharHeap[0]]:
                    heapq.heappop(activeCharHeap)
                if activeCharHeap:
                    smallestCharIndex = activeCharHeap[0]
                    charIndexStacks[smallestCharIndex].pop()
                    if not charIndexStacks[smallestCharIndex]:
                        heapq.heappop(activeCharHeap)
            else:
                charId = ord(char) - ord('a')
                if not charIndexStacks[charId]:
                    heapq.heappush(activeCharHeap, charId)
                charIndexStacks[charId].append(index)

        resultIndices = []
        for charStack in charIndexStacks:
            resultIndices.extend(charStack)
        
        resultIndices.sort()
        return ''.join(s[i] for i in resultIndices)
