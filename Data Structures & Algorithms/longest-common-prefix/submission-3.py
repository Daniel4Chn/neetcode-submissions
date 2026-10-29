class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if len(strs[j]) <= i:
                    return prefix
                if strs[j][i] != strs[0][i]:
                    return prefix
            print(prefix)
            prefix+=strs[0][i]
        return prefix