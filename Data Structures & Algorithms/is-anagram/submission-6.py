class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOfS = {}
        for i in range(len(s)):
            if s[i] in mapOfS:
                mapOfS[s[i]]+=1
            else:
                mapOfS[s[i]] = 1
       
        for j in range(len(t)):
            if t[j] not in mapOfS:
                return False
            elif t[j] in mapOfS:
                if mapOfS[t[j]] <= 0:
                    return False
                else:
                    mapOfS[t[j]]-=1
        
        for k,v in mapOfS.items():
            if v != 0:
                return False
        return True        