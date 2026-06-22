class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #i+j = half. bin search i
        #[1, 3, 6, 8, 20] and [2, 7, 13, 17, 26, 30]
        #[1, 2, 3, 6, 7, (8), 13, 17, 20, 27, 30]
        len1, len2 = len(nums1), len(nums2)
        lentotal = len1 + len2
        lenhalf = lentotal // 2
        low = max(0, lenhalf - len2)
        high = min(len1, lenhalf)
        while True:
            i = (high - low) // 2 + low
            j = lenhalf - i
            L1 = nums1[i-1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < len1 else float('inf')
            L2 = nums2[j-1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < len2 else float('inf')
            if L1 <= R2 and L2 <= R1:
                break
            elif L1 > R2:
                high = i - 1
            elif L2 > R1:
                low = i + 1
        if lentotal % 2 == 0:
            return (max(L1, L2) +  min(R1, R2)) / 2
        else: 
            return min(R1, R2)
