class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            while i < j and self.isCharOrNot(s[i]) == False:
                i+=1
            while i < j and self.isCharOrNot(s[j]) == False:
                j-=1
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
        

    def isCharOrNot(self, s) -> bool:
        if ord('Z') >= ord(s) and ord(s) >= ord('A'):
            return True
        elif ord('z') >= ord(s) and ord(s) >= ord('a'):
            return True
        elif ord('9') >= ord(s) and ord(s) >= ord('0'):
            return True
        else:
            return False