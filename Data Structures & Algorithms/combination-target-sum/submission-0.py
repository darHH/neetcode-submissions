class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        combination = []

        def backtrack(start_index, remaining):
            # Found a valid combination
            if remaining == 0:
                results.append(list(combination))
                return
            if remaining < 0:
                return
            
            # start at start_index so we never revisit earlier
            # candidates that makes combination unique
            for i in range(start_index, len(nums)):
                combination.append(nums[i])
                # pass i, not i + 1 because duplicates is allowed
                backtrack(i, remaining - nums[i])
                combination.pop()
        
        backtrack(0, target)
        return results