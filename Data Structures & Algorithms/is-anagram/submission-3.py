class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = list(s)
        t_array = list(t)
        for letter in s_array:
            if letter in t_array:
                t_array.remove(letter)
            else:
                return False
        if len(t_array) == 0:
            return True
        return False