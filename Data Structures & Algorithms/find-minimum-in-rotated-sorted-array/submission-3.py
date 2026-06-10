class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find the first index of supposed end of the list, then answer is the index before
        #refer to this as the pair, the pair, if one exist, will always contain the smallest val
        #if does not exist, the smallest value is nums[0]
        if len(nums) == 1:
            return nums[0]

        lp, rp = 0, len(nums) - 1
        while lp < rp:
            mp = (rp - lp) // 2 + lp
            #left side is all sorted and the pair may be in the right
            if nums[mp] > nums[rp]:
                lp = mp + 1
            #pair may be in the left
            else:
                rp = mp
        return nums[lp]

