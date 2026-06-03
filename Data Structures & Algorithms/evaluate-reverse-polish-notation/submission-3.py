class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] == '+':
                temp = int(stack.pop(-2)) + int(stack.pop(-1))
                stack.append(temp)
            elif tokens[i] == '-':
                temp = int(stack.pop(-2)) - int(stack.pop(-1))
                stack.append(temp)
            elif tokens[i] == '*':
                temp = int(stack.pop(-2)) * int(stack.pop(-1))
                stack.append(temp)     
            elif tokens[i] == '/':
                temp = int(int(stack.pop(-2)) / int(stack.pop(-1)))
                stack.append(temp)
            else: 
                stack.append(int(tokens[i]))
        return stack[0]