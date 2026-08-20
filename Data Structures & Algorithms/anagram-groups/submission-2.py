from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        allAnagrams = defaultdict(list)
        for i in range(len(strs)):
            chars = [0]*26
            for char in strs[i]:
                chars[ord(char)-ord('a')]+=1
            allAnagrams[tuple(chars)].append(strs[i])
        
        for k,v in allAnagrams.items():
            res.append(v)
        return res
        


