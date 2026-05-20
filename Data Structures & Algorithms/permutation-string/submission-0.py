class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed sliding window of len 3 to check if all chars in s1 are matching
        # time complexity should be O(n)
        lp = 0
        rp = len(s1) - 1
        list_s1 = list(s1)
        sorted_s1 = sorted(list_s1)
        while rp < len(s2):
            sorted_window = sorted(list(s2)[lp:rp + 1])
            if sorted_window == sorted_s1:
                return True
            lp +=1 
            rp +=1
        return False
