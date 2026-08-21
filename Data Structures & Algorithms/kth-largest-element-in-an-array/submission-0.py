class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initial thought 1: use heap or sort list but that is that allowed
        nums.sort(reverse=True)
        # print(nums)
        return nums[k-1]
          