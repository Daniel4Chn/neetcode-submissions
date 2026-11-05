class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda interval:interval[0])
        print(intervals)
        res = []
        tempInterval = intervals[0]
        for i in range(1, len(intervals)):
            if tempInterval[1] < intervals[i][0]:
                res.append(tempInterval)
                tempInterval = intervals[i]
                continue
            elif tempInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                tempInterval = [min(tempInterval[0], intervals[i][0]), max(tempInterval[1], intervals[i][1])]
        
        res.append(tempInterval)
        return res