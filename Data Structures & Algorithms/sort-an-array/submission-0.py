class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # helper to merge two sorted arrays
        def merge_two_arrays(A: List[int], B: List[int]) -> List[int]:
            ap, bp = 0, 0
            output = []
            while ap < len(A) and bp < len(B):
                if A[ap] < B[bp]:
                    output.append(A[ap])
                    ap += 1
                else:
                    output.append(B[bp])
                    bp += 1
            # ap or bp has reached end of their list
            if ap < len(A):
                output.extend(A[ap:])
            elif bp < len(B):
                output.extend(B[bp:])
            return output

        nums_length = len(nums)
        mid = nums_length // 2

        if nums_length <= 1: 
            return nums
        
        return merge_two_arrays(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
        
