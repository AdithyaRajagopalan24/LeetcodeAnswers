class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n + 1):
            current_height = heights[i] if i < n else 0
            while stack and heights[stack[-1]] > current_height:
                h_index = stack.pop()
                H = heights[h_index]
                R = i
                L = stack[-1] if stack else -1
                width = R - L - 1
                area = H * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area