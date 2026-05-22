class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        r = 0
        setOfChars = set()
        longest = 0
        curr = 0
        while r < len(s):
            if s[r] not in setOfChars:
                print("hello")
                setOfChars.add(s[r])
                r+=1
                curr +=1
                longest = max(curr, longest)
                
            else:
                while l < r:
                    if s[l] == s[r]:
                        setOfChars.remove(s[l])
                        setOfChars.add(s[r])
                        l+=1
                        r+=1
                        break
                    else:
                        setOfChars.remove(s[l])
                        l+=1
                        curr -=1

        return longest
            