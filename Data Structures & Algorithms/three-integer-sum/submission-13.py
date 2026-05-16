class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        seen = []
        for i in range(0, len(nums) - 1):
            target = -nums[i]
            if target not in seen:
                sp, ep = i + 1, len(nums) - 1
                seen.append(target)
                while ep > sp:
                    if nums[sp] + nums[ep] < target:
                        sp += 1
                    elif nums[sp] + nums[ep] > target:
                        ep -= 1
                    else:
                        curr = sorted([nums[sp], nums[ep], nums[i]])
                        output.append(curr)
                        sp += 1
                        ep -= 1
                        while ep > sp and nums[ep] == nums[ep + 1]:
                            ep -= 1
                        while ep > sp and nums[sp] == nums[sp - 1]:
                            sp += 1
            else:
                continue
        return output