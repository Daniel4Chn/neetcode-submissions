class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubString = s[0]
        for i in range(1,len(s)):
            substring = s[i]
            l = i-1
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substring = s[l:r+1]
                l-=1
                r+=1
            if len(substring) > len(longestSubString):
                longestSubString = substring
            firstI = i-1
            
            if s[firstI] == s[i]:
                substring = s[firstI:i+1]
                l = firstI-1
                r = i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    substring = s[l:r+1]
                    l-=1
                    r+=1
                if len(substring) > len(longestSubString):
                    longestSubString = substring
            
        return longestSubString