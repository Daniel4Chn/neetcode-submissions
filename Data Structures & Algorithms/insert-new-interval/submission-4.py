class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            interval1 = intervals[i]

            if i == 0:
                if newInterval[1] < interval1[0]:
                    intervals.insert(i, newInterval)
                    return intervals

            if i == len(intervals)-1: 
                if newInterval[0] > interval1[1]:
                    intervals.append([newInterval[0], newInterval[1]])
                    break
                    
            if newInterval[1] >= interval1[0] and newInterval[0] <= interval1[1]:
                intervals[i][0] = min(interval1[0], newInterval[0])
                intervals[i][1] = max(interval1[1], newInterval[1])
                break


            elif i < len(intervals)-1:
                if intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[1]:
                    intervals.insert(i+1, newInterval)
                    return intervals

        lengthOfInitial = len(intervals)
        j = 0
        while j < lengthOfInitial-1:
            intervals1 = intervals[j]
            intervals2 = intervals[j+1]
            if intervals1[1] >= intervals2[0]:
                intervals.pop(j)
                intervals.pop(j)
                lengthOfInitial-=1
                intervals.insert(j, [intervals1[0], max(intervals1[1],intervals2[1])])
            else:
                j+=1
        return intervals
