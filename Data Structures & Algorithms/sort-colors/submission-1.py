class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep three pointers that seperate the array into three regions
        # [0, low) for 0s, [low, mid] for 1s, (high, length) for 2s
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                if mid == low:
                    mid += 1
                else:
                    low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                high -= 1

        return nums
