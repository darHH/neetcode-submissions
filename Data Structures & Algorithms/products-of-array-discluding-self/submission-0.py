class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        num_of_zeros = 0
        for num in nums:
            if num != 0:
                total_product = total_product * num
            else:
                num_of_zeros += 1
        output = []
        print(total_product)
        for num in nums:
            if num != 0:
                if num_of_zeros >= 1:
                    output.append(0)
                else:
                    output.append(int(total_product / num))
            else:
                if num_of_zeros >= 2:
                    output.append(0)
                else:
                    output.append(total_product)
        return output