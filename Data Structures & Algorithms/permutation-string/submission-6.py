class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charsA = {}
        charsBWindow = {}
        if len(s2) < len(s1):
            return False

        for char in s1:
            charsA[char] = charsA.get(char,0) + 1
        
        for i in range(len(s1)):
            charsBWindow[s2[i]] = charsBWindow.get(s2[i],0) + 1
            
        if charsA == charsBWindow:
            return True
        l = 0
        for j in range(len(s1), len(s2)):
            charsBWindow[s2[l]]-=1
            if charsBWindow[s2[l]] == 0:
                charsBWindow.pop(s2[l], None)
            l+=1
            charsBWindow[s2[j]] = charsBWindow.get(s2[j],0)+1
           
            if charsA == charsBWindow:
                return True
        return False

