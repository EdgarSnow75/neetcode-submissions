class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit = 0
        for i in range(len(prices[1:]) + 1):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            elif profit < (prices[i] - lowest_price):
                profit = prices[i] - lowest_price
        return profit
            
        