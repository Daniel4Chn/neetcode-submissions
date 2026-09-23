from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        listOfElems = [[]for i in range(len(nums)+1)]
        freqCount = defaultdict(int)
        for i in nums:
            freqCount[i] += 1
        for key,v in freqCount.items():
            listOfElems[v].append(key)
        while k > 0:
            for i in range(len(listOfElems)-1,-1,-1):
                if k > 0:
                    for elem in listOfElems[i]:
                        if k > 0:
                            res.append(elem)
                            k-=1
                else:
                    break
        return res