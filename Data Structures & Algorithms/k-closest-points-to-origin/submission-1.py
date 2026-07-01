class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        listOfPDist = []
        heapq.heapify(listOfPDist)

        for point in points:
            
            distanceFromOrigin = math.sqrt(((point[0]**2) + (point[1]**2)))
            heapq.heappush(listOfPDist, [distanceFromOrigin, point])
        res = []
        while k > 0:
            coordinate = heapq.heappop(listOfPDist)
            res.append(coordinate[1])
            k-=1
        return res