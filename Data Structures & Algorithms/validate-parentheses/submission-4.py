class Solution:
    def isValid(self, s: str) -> bool:
        length_s = len(s)
        temp = []
        if length_s % 2 != 0 or length_s == 0:
            return False
        for letter in s:
            if letter == '(' or letter == '{' or letter == '[':
                temp.append(letter)
            elif len(temp) == 0:
                return False
            elif letter == ')' and temp.pop() != '(':
                return False
            elif letter == '}' and temp.pop() != '{':
                return False
            elif letter == ']' and temp.pop() != '[':
                return False
        if len(temp) == 0:
            return True
        else:
            return False