class Solution:
    def isValid(self, s: str) -> bool:
        stackOfParenthesis = []
        validParenthesis = {'}':'{',')':'(',"]":"["}
        for i in s:
            if i in validParenthesis:
            
                if len(stackOfParenthesis) != 0 and stackOfParenthesis[-1] == validParenthesis[i]:
                    stackOfParenthesis.pop()
                else:
                    return False
            else:
                stackOfParenthesis.append(i)
        return len(stackOfParenthesis) == 0