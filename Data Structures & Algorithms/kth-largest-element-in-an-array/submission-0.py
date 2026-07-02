from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        sortedOrder = nums
        heapify(nums)
        while len(sortedOrder) > k:
            print(len(sortedOrder))
            heapq.heappop(sortedOrder)
            
        return heapq.heappop(sortedOrder)