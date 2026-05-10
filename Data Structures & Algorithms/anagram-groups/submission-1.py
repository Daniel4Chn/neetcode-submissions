from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        dictOfWords = defaultdict(list)
        for stri in strs:
            arrOfChars = [0]*26
            for char in stri:
                arrOfChars[ord(char)-ord('a')] +=1
            dictOfWords[tuple(arrOfChars)].append(stri)
        
        for key, value in dictOfWords.items():
            output.append(value)
        return output


