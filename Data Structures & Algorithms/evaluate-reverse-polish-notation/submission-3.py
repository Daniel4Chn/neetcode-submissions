class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = []
        for token in tokens:
            if token == "+":
                op1 = operands.pop()
                op2 = operands.pop()
                operands.append(op1+op2)
            elif token == "*":
                op1 = operands.pop()
                op2 = operands.pop()
                operands.append(op1*op2)
            elif token == "-":
                op1 = operands.pop()
                op2 = operands.pop()
                operands.append(op2-op1)
            elif token == "/":
                op1 = operands.pop()
                op2 = operands.pop()
                operands.append(int(op2/op1))
            else:
                operands.append(int(token))
        return operands[-1]