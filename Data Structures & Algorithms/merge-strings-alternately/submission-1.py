class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalStr = ""

        l1 = 0
        r1 = len(word1)-1

        l2 = 0
        r2 = len(word2)-1

        while l1 <= r1 and l2 <= r2:
            finalStr+=word1[l1]
            l1+=1
            finalStr+=word2[l2]
            l2+=1
        
        if l1<=r1:
            finalStr+=word1[l1:r1+1]
        if l2<=r2:
            finalStr+=word2[l2:r2+1]
        return finalStr