class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #if new interval's end value is less than intervals start value then new interval is before that
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:len(intervals)])
                return res
            #if new interval's end value is greater than the current interval's start value it means it either overlaps or is way after the current interval
            #that's why you check whether the start value is greater of the new interval is greater than the current interval's end value 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res

