class Solution:
    def trap(self, height: List[int]) -> int:
        # for each bar, check if there are, 
        # and find the highest bar to its left and right.
        total_collected = 0
        for i in range(1, len(height) - 1):
            s_pointer, e_pointer = 0, len(height)
            s_height, e_height = height[i], height[i]
            for j in range(s_pointer, i):
                if height[j] > s_height:
                    s_height = height[j]
            for k in range(i + 1, e_pointer):
                if height[k] > e_height:
                    e_height = height[k]
            total_collected += min(s_height, e_height) - height[i]
        return total_collected




