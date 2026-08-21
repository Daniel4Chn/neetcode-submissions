from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arrOfFreq = [[]for i in range(len(nums)+1)]
        numberOfElems = defaultdict(int)
        for i in nums:
            numberOfElems[i]+=1
        
        for key, v in numberOfElems.items():
            arrOfFreq[v].append(key)
        
        res = []
        
        for i in range(len(arrOfFreq)-1,-1,-1):
            if k <= 0:
                return res
            
            for num in arrOfFreq[i]:
                print(k)
                print(num)
                res.append(num)
                k-=1
                if k <= 0:
                    break
        return res
            
        
        