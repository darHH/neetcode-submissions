class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         # thought process just use the first word and
         # go through list once
        curr = strs[0]
        for word in strs[1:]:
            for i in range(len(curr)):
                # print("for word:", word, "and curr", curr, "and i:", i)
                if i >= len(word):
                    curr = word
                    # print("curr exceed word")
                    break
                if curr[i] != word[i]:
                    curr = curr[:i]
                    # print("mismatch, new curr:", curr)
                    break
        return curr
