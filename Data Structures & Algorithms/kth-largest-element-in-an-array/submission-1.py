import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initial thought 1: use heap or sort list but is that allowed
        # i will use python's in built min heap but with negative numbers to make it a max heap
        # pop the largest and take the kth pop
        neg_nums = list(map(lambda x: -x, nums))
        heapq.heapify(neg_nums)
        for _ in range(k - 1):
            heapq.heappop(neg_nums)
        
        return -heapq.heappop(neg_nums)