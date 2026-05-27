class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        decStack = []
        for i in range(len(temperatures)):
            if len(decStack) == 0:
                decStack.append((temperatures[i],i))
            else:
                while len(decStack) > 0 and decStack[-1][0] < temperatures[i]:
                    topTemp = decStack.pop() 
                    res[topTemp[1]] = i-topTemp[1]
                decStack.append((temperatures[i],i))
        return res