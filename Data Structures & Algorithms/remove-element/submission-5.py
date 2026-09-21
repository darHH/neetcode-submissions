class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # keep two pointers, start and end
        # increment start, if start sees a val, 
        # swap with end and decrement end
        start, end = 0, len(nums) - 1
        if len(nums) == 0:
            return 0

        while start < end:
            if nums[end] == val:
                end -= 1
                # print("-end:", start, end)
            elif nums[start] == val:
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                start += 1
                end -= 1
                # print("+start", start, end)
            else:
                start += 1
                
        if nums[start] == val:
            return start
        else:
            return start + 1
                