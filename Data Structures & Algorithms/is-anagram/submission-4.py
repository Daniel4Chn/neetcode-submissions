class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOfS = {}
        for i in range(len(s)):
            if s[i] in mapOfS:
                mapOfS[s[i]]+=1
            else:
                mapOfS[s[i]] = 1
        
        mapOfT = {}
        for j in range(len(t)):
            if t[j] in mapOfT:
                mapOfT[t[j]]+=1
            else:
                mapOfT[t[j]] = 1
        
        if mapOfS == mapOfT:
            return True
        else:
            return False
        