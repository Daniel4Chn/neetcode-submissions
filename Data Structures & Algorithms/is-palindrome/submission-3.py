class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        newStr = ""
        for c in s:
            if c and self.isCharOrNum(c):
                newStr+=c
        l = 0
        r = len(newStr)-1
        while l < r:
            if newStr[l] == newStr[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            

        
    def isCharOrNum(self,cha: chr) -> bool:
        if ord(cha) <= ord('9') and ord(cha) >= ord('0'):
            return True
        elif ord(cha) >= ord('a') and ord(cha) <= ord('z'):
            return True
        else:
            return False
