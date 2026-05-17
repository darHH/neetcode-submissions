class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        # dp/greedy
        sp, ep = 0, len(heights) - 1
        while ep > sp: 
            temp = (ep - sp) * min(heights[sp], heights[ep])
            if temp > output:
                output = temp
            if heights[sp] > heights[ep]:
                ep -= 1
            else:
                sp += 1

        return output
