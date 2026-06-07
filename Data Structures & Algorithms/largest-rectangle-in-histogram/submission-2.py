class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            curr_height = heights[i]
            curr_width = 1
            lp, rp = i - 1, i + 1
            while lp >= 0:
                if heights[lp] < curr_height:
                    break
                else:
                    curr_width +=1 
                lp -= 1
            while rp < len(heights):
                if heights[rp] < curr_height:
                    break
                else: 
                    curr_width +=1 
                    rp += 1
            curr_area = curr_height * curr_width
            if curr_area > max_area:
                max_area = curr_area
        return max_area