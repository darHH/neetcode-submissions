class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1
        while rp >= lp:
            mp = (rp - lp) // 2 + lp
            print(lp, rp, mp)
            if nums[mp] == target:
                return mp
            elif nums[mp] > target:
                rp = mp - 1
            else:
                lp = mp + 1
        return -1
