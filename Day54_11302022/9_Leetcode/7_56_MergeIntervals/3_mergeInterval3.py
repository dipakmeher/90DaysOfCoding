# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

#Functions
def mergeIntervals(intervals):
    res = []
    intervals.sort()
    n = len(intervals)
    res.append(intervals[0])

    for start,end in intervals[1:]:
        lastEnd = res[-1][1]
        if(lastEnd>=start):
            res[-1][1] = max(lastEnd,end)
        else:
            res.append([start,end])
    return res

#Drivers Code
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals)
print(mergeIntervals(intervals))  