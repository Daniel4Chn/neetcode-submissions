class TimeMap:

    def __init__(self):
        self.tableOfTime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.tableOfTime:
            self.tableOfTime[key] = []
        
        self.tableOfTime[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.tableOfTime:
            return ""
        
        l = 0
        r = len(self.tableOfTime[key])-1
        while l<=r:
            mid = (l+r)//2
            if self.tableOfTime[key][mid][1] < timestamp:
                l = mid+1
            elif self.tableOfTime[key][mid][1] > timestamp:
                r = mid-1
            else:
                return self.tableOfTime[key][mid][0]
        if r < 0:
            return ""
        
        return self.tableOfTime[key][r][0]
            

