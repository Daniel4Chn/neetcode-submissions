class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position: return 0
        sortedIncStack = []
        helperStack = []
        for i in range(len(position)):
            if not sortedIncStack:
                sortedIncStack.append((position[i], speed[i]))
            else:
                while sortedIncStack and position[i] < sortedIncStack[-1][0]:
                    helperStack.append(sortedIncStack.pop())
                sortedIncStack.append((position[i], speed[i]))
                while helperStack:
                    sortedIncStack.append(helperStack.pop())
        
        fleet = 0
        outputTimes = [0] * len(sortedIncStack)
        i = len(sortedIncStack)-1
        print(sortedIncStack)
        while sortedIncStack:
            poppedElem = sortedIncStack.pop()
            time = (target-poppedElem[0])/poppedElem[1]
            outputTimes[i] = time
            i-=1
        if len(outputTimes) == 1:
            return 1
        maxTime = 0
        for i in range(len(outputTimes)-1,-1,-1):
            if outputTimes[i] > maxTime:
                fleet+=1
                maxTime = outputTimes[i]
        
        return fleet
        

        