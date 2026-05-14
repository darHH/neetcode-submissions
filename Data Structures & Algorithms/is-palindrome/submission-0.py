class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = s[::-1]
        # clean_reverse_s = "".join(reverse_s.lower().split())
        # clean_og_s = "".join(s.lower().split())
        clean_reverse_s = ""
        clean_og_s = ""
        for letter in reverse_s:
            if letter.isalnum():
                clean_reverse_s = clean_reverse_s + letter.lower()
        for letter in s:
            if letter.isalnum():
                clean_og_s = clean_og_s + letter.lower()
        return clean_reverse_s == clean_og_s