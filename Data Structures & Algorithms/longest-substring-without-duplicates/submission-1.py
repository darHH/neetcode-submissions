class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        curr_count = 0
        max_count = 0
        sp = 0
        for ep in range(0, len(s)):
            if s[ep] not in seen:
                # print("seen:", s[ep], "at:", ep)
                seen.add(s[ep])
            else:
                curr_count = ep - sp
                max_count = max(max_count, curr_count)
                # print("dup reached, curr count:", curr_count)
                for i in range(sp, ep):
                    # print("removed from seen:", s[i])
                    seen.remove(s[i])
                    if s[i] == s[ep]:
                        sp = i + 1
                        seen.add(s[i])
                        # print("new sp:", sp)
                        break
        return max(max_count, len(s) - sp)

                
                
