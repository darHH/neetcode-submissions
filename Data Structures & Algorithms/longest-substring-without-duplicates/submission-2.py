class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_count = 0
        sp = 0
        for ep in range(0, len(s)):
            if s[ep] not in seen:
                seen.add(s[ep])
            else:
                max_count = max(max_count, ep - sp)
                for i in range(sp, ep):
                    seen.remove(s[i])
                    if s[i] == s[ep]:
                        sp = i + 1
                        seen.add(s[i])
                        break
        return max(max_count, len(s) - sp)

                
                
