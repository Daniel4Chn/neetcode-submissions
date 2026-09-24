class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longestSeq = 0
        l = 0
        r = 0
        setOfNums = set()
        while r < len(s):
            while r < len(s) and s[r] not in setOfNums:
                setOfNums.add(s[r])
                r+=1
            longestSeq = max(longestSeq, len(setOfNums))
            if r < len(s):
                while l < r and s[r] in setOfNums:
                    setOfNums.remove(s[l])
                    l+=1

        return longestSeq
