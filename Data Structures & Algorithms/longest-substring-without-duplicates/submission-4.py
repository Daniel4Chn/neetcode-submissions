class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        setOfChars = set()
        for r in range(len(s)):
            while s[r] in setOfChars:
                setOfChars.remove(s[l])
                l+=1
            setOfChars.add(s[r])
            longest = max(longest, r-l+1)
        

        return longest
            