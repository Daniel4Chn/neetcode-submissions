from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        for i in range(len(stones)):
            stones[i] = stones[i]*-1
        
        heapify(stones)

        while len(maxHeap) > 1:
            y = heappop(maxHeap) * -1
            x = heappop(maxHeap) * -1
            
            if x == y:
                continue
            if x < y:
                y = (y-x) *-1
                heappush(maxHeap, y)
                
                
                
        
        if len(maxHeap) == 0:
            return 0
        else:
            return heappop(maxHeap)*-1
            