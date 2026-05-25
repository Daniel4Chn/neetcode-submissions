class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        
        if len(self.minStack) == 0:
            self.minStack.append((val, val))
        else:
            if self.minStack[-1][1] >= val:
                self.minStack.append((val, val))
            else:
                self.minStack.append((val, self.minStack[-1][1]))

    def pop(self) -> None:
        
        self.minStack.pop()

    def top(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1][1]
        else:
            return None
