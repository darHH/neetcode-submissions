class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lp, rp = 0, 0
        freq = {}
        t_dict = {}

        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        print("T_DICT", t_dict)

        def isFreqValid() -> bool:
            for letter in t_dict:
                if freq.get(letter, 0) < t_dict[letter]:
                    return False
            return True
        
        # when i move rp, add to freq
        # when i move lp, remove from freq
        min_length = len(s) + 1
        min_substring = ""
        for rp in range(len(s)):
            freq[s[rp]] = freq.get(s[rp], 0) + 1
            # print("INVALID", lp, rp, freq)
            while isFreqValid():
                curr_length = rp - lp + 1
                if curr_length < min_length:
                    min_length = curr_length
                    min_substring = s[lp:rp + 1]
                freq[s[lp]] = freq.get(s[lp], 0) - 1
                # print("VALID", lp, rp, freq, min_substring)
                lp += 1

        return min_substring