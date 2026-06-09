import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min is 1, max is max of one pile
        #start with 1 and double up? no, will take forever if large value in pile

        #helper function to check hours required given a rate
        def hoursTakenToEat(eating_rate: int) -> int:
            output = 0
            piles_dup = piles.copy()
            while piles_dup:
                curr_pile = piles_dup.pop()
                output += math.ceil(curr_pile / eating_rate)
            # print("CHECKED EATING RATE", eating_rate, "TOOK:", output)
            return output 

        high_p = max(piles)
        low_p = 1
        while low_p < high_p:
            mid_p = (high_p - low_p) // 2 + low_p
            # print(high_p, low_p, mid_p, hoursTakenToEat(mid_p))
            if hoursTakenToEat(mid_p) <= h:
                high_p = mid_p
            else:
                low_p = mid_p + 1
        
        return high_p


