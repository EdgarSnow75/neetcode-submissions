class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit = 0
        for num in prices[1:]:
            if num < lowest_price:
                lowest_price = num
            elif profit < (num - lowest_price):
                profit = num - lowest_price
        return profit
            
        