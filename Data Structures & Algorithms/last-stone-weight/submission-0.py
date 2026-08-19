import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # initial thoughts: sort the array and keep "popping" the largest two until one is left.
        # but adding each stone after smashing will be O(log n) through bin search +O(n) to shift the array potentially
        # next thought: use a max heap
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)
        # print(heapq.heappop(neg_stones) * -1)
        while len(neg_stones) > 1:
            heaviest_stone = heapq.heappop(neg_stones) * -1
            next_heaviest_stone = heapq.heappop(neg_stones) * -1
            if heaviest_stone > next_heaviest_stone:
                new_stone = heaviest_stone - next_heaviest_stone
                temp = new_stone * -1
                heapq.heappush(neg_stones, temp)
        
        if len(neg_stones) >= 1:
            return neg_stones[0] * -1
        else:
            return 0