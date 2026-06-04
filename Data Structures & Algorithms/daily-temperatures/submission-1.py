class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack which contains consecutive days in ascending order of temperature
        # start iterating from the back
        # second attempt with an actual stack, optimize time 
        # now stack keeps indices
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # if stack not empty, highest is the next warmer day
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)
        return answer
