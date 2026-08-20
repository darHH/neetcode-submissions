import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # initial thoughts: create a heap with tuples as its elements
        # first value of each tuple will be the eucl distance.
        # this is the value that the heap uses to compare too
        heap = []
        answer = []
        for point in points:
            dist_to_origin = math.sqrt((point[0])**2 + (point[1])**2)
            temp_tuple = (dist_to_origin, point[0], point[1])
            heapq.heappush(heap, temp_tuple)
            # print(heap)
        for _ in range(k):
            closest_tuple = heapq.heappop(heap)
            closest_point = [closest_tuple[1], closest_tuple[2]] 
            answer.append(closest_point)
        return answer