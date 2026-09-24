class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentPrice = prices[0]
        maxProfit = 0
        for price in range(len(prices)):
            if prices[price] < currentPrice:
                currentPrice = prices[price]
            elif prices[price] > currentPrice:
                maxProfit = max(maxProfit, prices[price]-currentPrice)
        
        return maxProfit
