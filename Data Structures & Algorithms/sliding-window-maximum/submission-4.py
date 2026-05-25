class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        highest_window = [] # stores indexes of num
        lp = 0
        output = []
        for i in range(len(nums)):
            while lp < len(highest_window) and highest_window[lp] <= i - k:
                lp += 1
            while lp < len(highest_window) and nums[highest_window[-1]] < nums[i]:
                highest_window.pop()
            
            highest_window.append(i)

            if i >= k - 1:
                output.append(nums[highest_window[lp]])

        return output