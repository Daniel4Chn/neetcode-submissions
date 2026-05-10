from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        mapOfValues = defaultdict(int)
        for elem in nums:
            mapOfValues[elem] +=1
        
        arr = [[] for i in range(len(nums)+1)]
        for key,value in mapOfValues.items():
            arr[value].append(key)

        c = len(arr)
        for i in range(c-1,-1,-1):
            for j in arr[i]:
                if k > 0:
                    output.append(j)
                    k-=1
                else:
                    break
        return output