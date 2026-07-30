class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) < len(needle):
            return -1

        for j in range(len(haystack)):
            i = 0
            k = j
            var = False
            if haystack[j] == needle[0] and len(haystack)-j >= len(needle):
                while i < len(needle) and k < len(haystack):
                    var = True
                    if haystack[k] != needle[i]:
                        var = False
                        break
                    i+=1
                    k+=1
                if var:
                    return j
        return -1
