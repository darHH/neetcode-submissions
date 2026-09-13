class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. sort the weights to get lightest and heaviest person in O(1)
        people.sort()

        lightest_idx = 0
        heaviest_idx = len(people) - 1
        boat_count = 0

        while lightest_idx <= heaviest_idx:
            # if lightest + heaviest can fit, add both as 1 boat count 
            if people[lightest_idx] + people[heaviest_idx] <= limit:
                lightest_idx += 1

            boat_count += 1
            heaviest_idx -= 1
        
        return boat_count