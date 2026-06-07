class Solution:
    #try stack approach -> keep stack of indices of height which is increasing
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                curr_idx = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                width = right - left - 1
                curr_area = heights[curr_idx] * width
                max_area = max(max_area, curr_area)
            stack.append(i)

        while stack:
            curr_idx = stack.pop()
            left = stack[-1] if stack else -1
            right = len(heights)
            width = right - left - 1
            curr_area = heights[curr_idx] * width
            max_area = max(max_area, curr_area)

        return max_area
