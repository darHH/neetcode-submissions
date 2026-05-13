class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # sort the list O(nlogn) and count longest subsequence in one pass O(n)
        unique_nums = set(nums)
        sorted_nums = sorted(unique_nums)
        highest_count = 1
        current_count = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                current_count += 1 
            else:
                if current_count >= highest_count:
                    highest_count = current_count
                current_count = 1
        return max(current_count, highest_count)
             
                    
        
