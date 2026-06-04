class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack which contains consecutive days in ascending order of temperature
        # start iterating from the back
        stack = []
        answer = []
        for i in range(len(temperatures) - 1, -1, -1):
            print("STACK AT", i, "IS:", stack)
            temp = 0
            if len(stack) == 0:
                answer.append(0)
            else:
                for j in range(len(stack) -1, -1, -1):
                    temp += 1
                    isAnyHigher = False
                    if stack[j] > temperatures[i]:
                        # print("FOUND HIGHER TEMP:", stack[j], "AT:", j, "AFTER:", temp, "DAYS")
                        answer.append(temp)
                        isAnyHigher = True
                        break
                if not isAnyHigher:
                    answer.append(0)
                isAnyHigher = False
            stack.append(temperatures[i])   
        answer.reverse()
        return answer
