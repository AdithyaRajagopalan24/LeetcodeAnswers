class Solution:
    def trap(self, height: List[int]) -> int:
        waterHeights = []
        curWaterheight = 0
        curQuantity = 0
        maxvalIndex = height.index(max(height))
        for i in range(maxvalIndex+1):
            if height[i] >= curWaterheight:
                waterHeights.append(curQuantity)
                curWaterheight = height[i]
                curQuantity = 0
            else:
                curQuantity += (curWaterheight - height[i])
        curWaterheight = 0
        for i in range(len(height)-1, maxvalIndex-1, -1):
            if height[i] >= curWaterheight:
                waterHeights.append(curQuantity)
                curWaterheight = height[i]
                curQuantity = 0
            else:
                curQuantity += (curWaterheight - height[i])
        return sum(waterHeights)    