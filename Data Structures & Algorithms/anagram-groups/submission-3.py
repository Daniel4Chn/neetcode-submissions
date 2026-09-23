from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapOfAnagrams = defaultdict(list)
        for i in strs:
            charArr = [0]*26
            for char in i:
                charArr[ord(char)-ord('a')]+=1
            
            mapOfAnagrams[tuple(charArr)].append(i)
        
        for k,v in mapOfAnagrams.items():
            res.append(v)
        return res


