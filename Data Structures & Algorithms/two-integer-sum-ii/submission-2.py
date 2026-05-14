class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sp = 0 
        ep = len(numbers) - 1
        while ep > sp:
            
            if numbers[sp] + numbers[ep] < target:
                sp += 1
            elif numbers[sp] + numbers[ep] > target: 
                ep -= 1
            else:
                return [sp + 1, ep + 1]
            
