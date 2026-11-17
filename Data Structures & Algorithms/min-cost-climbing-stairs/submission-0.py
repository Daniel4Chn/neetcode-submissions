class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimumCost = float('inf')
        if len(cost) <= 2:
            return min(cost)
        
        cache = [0 for i in range(len(cost)+1)]
        cache[-1] = cost[-1]
        cache[-2] = cost[-2]

        
        i = len(cost)-2
        while i > 0:
            cache[i] = cost[i-1] + min(cache[i+1], cache[i+2])
            i-=1
        cache[0] = min(cache[1], cache[2])
        return cache[0]
        