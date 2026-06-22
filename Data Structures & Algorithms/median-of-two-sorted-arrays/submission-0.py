class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #inithoughts - some sort of math median trick, taking the median of two medians gives the overall median?
        #merging both arrays is O(m+n)
        #then bin search both arrays is O(log(m+n))
        p1, p2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        sorted_array = []
        while p1 < len1 and p2 < len2:
            if nums1[p1] >= nums2[p2]:
                sorted_array.append(nums2[p2])
                p2 += 1
            else:
                sorted_array.append(nums1[p1])
                p1 += 1
        while p1 < len1:
            sorted_array.append(nums1[p1])
            p1 += 1
        while p2 < len2:
            sorted_array.append(nums2[p2])
            p2 += 1
        print(sorted_array)
        #take the median
        len_array = len(sorted_array)
        if len_array % 2 == 0:
            return (sorted_array[len_array // 2 - 1] + sorted_array[len_array // 2]) / 2
        else:
            # print(len_array // 2 + 1)
            return sorted_array[len_array // 2]
