class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_max_index = 0
        curr_max_value = -10000
        lp = 0 
        rp = k - 1
        output = []
        for i in range(k):
            if nums[i] > curr_max_value:
                curr_max_index = i
                curr_max_value = nums[i]
        if len(nums) <= k:
            return [curr_max_value]
        for j in range(rp, len(nums)):
            if nums[rp] > curr_max_value:
                curr_max_index = j
                curr_max_value = nums[rp]
            output.append(curr_max_value)
            print(rp, curr_max_index, curr_max_value)
            lp += 1 
            rp += 1 
            if lp > curr_max_index:
                curr_max_value = -10000
                for k in range(lp, rp):
                    if nums[k] > curr_max_value:
                        curr_max_index = k
                        curr_max_value = nums[k]
        return output
                    