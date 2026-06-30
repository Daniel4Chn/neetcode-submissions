from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.stream = nums
        heapify(self.stream)
        self.numberToFind = k
        while len(self.stream) > self.numberToFind:
            heappop(self.stream)
        
    
    def add(self, val: int) -> int:

        heappush(self.stream, val)
        if len(self.stream) > self.numberToFind:
            heappop(self.stream)
        return self.stream[0]
        

