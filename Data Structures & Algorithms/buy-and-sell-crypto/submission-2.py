class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of lowest seen
        lowest_seen = prices[0]
        highest_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest_seen:
                lowest_seen = prices[i]
            curr_profit = prices[i] - lowest_seen
            highest_profit = max(curr_profit, highest_profit)
            # print("curr_price:", prices[i], "lowest seen:", lowest_seen, "curr_profit:", curr_profit)
        return highest_profit