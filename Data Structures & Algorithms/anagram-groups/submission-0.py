class Solution:
    def isAnagram(self, wordA, wordB):
        if len(wordA) != len(wordB):
            return False
        array_wordB = list(wordB)
        for letter in wordA:
            if letter in array_wordB:
                array_wordB.remove(letter)
            else:
                return False
        return True
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        while len(strs) != 0:
            current_word = strs[0]
            temp = []
            remaining = []
            for word in strs:
                if self.isAnagram(word, current_word):
                    temp.append(word)
                else:
                    remaining.append(word)
            output.append(temp)
            strs = remaining
            
        return output

            