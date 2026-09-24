class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and self.isValid(s[l]) == False:
                l+=1
            
            while l < r and self.isValid(s[r]) == False:
                r-=1
            print(s[l])
            print(s[r])
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True 
    

    def isValid(self, char):
        if (ord('Z') >= ord(char) and ord('A') <= ord(char)):
            return True
        elif ((ord('z')) >= ord(char) and ord(char) >= ord('a')):
            return True
        elif (ord('9') >= ord(char) and ord('0') <= ord(char)):
            return True
        else:
            return False