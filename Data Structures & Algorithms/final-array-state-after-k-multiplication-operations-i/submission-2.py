from heapq import heapify, heappop, heappush
class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        newArr = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            newArr[i] = (nums[i], i)
            
        heapify(newArr)
        for i in range(k):
            minValue = heapq.heappop(newArr)
            minValue = (minValue[0]*multiplier, minValue[1])
            heapq.heappush(newArr, minValue)
            nums[minValue[1]] = minValue[0]
        return nums

