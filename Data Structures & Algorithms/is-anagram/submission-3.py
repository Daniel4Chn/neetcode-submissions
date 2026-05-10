class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if both strings have different lengths then that means they aren't anagrams of each other
        if len(s) != len(t):
            return False

        mapOfS = dict()
        mapOfT = dict()

        for char in s:
            if char in mapOfS:
                mapOfS[char] +=1
            else:
                mapOfS[char] = 1
        
        for char in t:
            if char in mapOfT:
                mapOfT[char] +=1
            else:
                mapOfT[char] = 1
        
        return mapOfT == mapOfS
        