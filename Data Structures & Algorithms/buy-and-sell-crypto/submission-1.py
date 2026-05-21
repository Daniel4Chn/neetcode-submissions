class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        picked = -999
        for i in range(len(prices)):
            
            if i == 0:
                picked = prices[i]
                continue
            
            if prices[i] > picked:
                maxProfit = max(maxProfit, prices[i]-picked)
            else:
                picked = prices[i]
        return maxProfit