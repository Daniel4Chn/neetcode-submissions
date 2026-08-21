class Solution:
    def isValid(self, s: str) -> bool:
        mapOfValidParen = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for i in s:
            if i in mapOfValidParen:
                if len(stack) > 0:
                    if stack[-1] == mapOfValidParen[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        else:
            return True
       