class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElem = float('-inf')
        
        for i in piles:
            maxElem = max(maxElem, i)
            
        left = 1
        right = maxElem
        bestRate = float('inf')
        while left <= right:
            rate = (left+right)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/rate)
            if hours > h:
                left = rate+1
            elif hours <= h:
                bestRate = min(bestRate, rate)
                right = rate-1
        return bestRate

            
