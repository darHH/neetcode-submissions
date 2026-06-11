class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search_on_sorted(lp: int, rp: int) -> int:
            while lp <= rp:
                mp = (rp - lp) // 2 + lp
                if nums[mp] == target:
                    return mp
                elif nums[mp] < target:
                    lp = mp + 1
                else:
                    rp = mp - 1
            return -1
        
        #find the two sorted segments
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            mp = (rp - lp) // 2 + lp
            if nums[mp] > nums[rp]:
                lp = mp + 1
            else:
                rp = mp
        #nums[lp] contains min value

        return max(bin_search_on_sorted(lp, len(nums) - 1), bin_search_on_sorted(0, lp - 1))


    