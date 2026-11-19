class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i]*-1
        
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 == stone2:
                continue
            else:
                newWeight = stone1-stone2
                heapq.heappush(stones, newWeight)
        if len(stones) == 0:
            return 0
        return stones[0]*-1