class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0 
        rp = 0
        max_length = 0
        freq = {}
        while rp < len(s):
            freq[s[rp]] = freq.get(s[rp], 0) + 1
            if ((rp - lp + 1) - max(freq.values())) > k:
                freq[s[lp]] -= 1
                lp += 1
            max_length = max(max_length, rp - lp + 1)
            rp += 1

        return max_length
