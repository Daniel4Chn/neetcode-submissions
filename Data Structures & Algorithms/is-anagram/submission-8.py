class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrOfChars = {}
        for string in s:
            arrOfChars[string] = 1 + arrOfChars.get(string, 0)
        for string in t:
            if string not in arrOfChars:
                return False
            if arrOfChars[string] == 0:
                return False
            arrOfChars[string]-=1
        for k,v in arrOfChars.items():
            if v != 0:
                return False
        return True