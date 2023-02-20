# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

#Functions
def mergeIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x [0])
    print("intervals: ",intervals)
    ans = []

    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    return ans

#Drivers Code
intervals = [[1,3],[8,10],[2,6],[15,18]]
print("Original Interval: ", intervals)
print(mergeIntervals(intervals))  

