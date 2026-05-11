class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count_dict = {}
        for num in nums:
            if num in num_to_count_dict:
                num_to_count_dict[num] += 1
            else:
                num_to_count_dict[num] = 0
        sorted_dict = dict(sorted(num_to_count_dict.items(), key=lambda x: x[1], reverse=True))
        output = []
        list_dict = list(sorted_dict.keys())
        return list_dict[0:k]