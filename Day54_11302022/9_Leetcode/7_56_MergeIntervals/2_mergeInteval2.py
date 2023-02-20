# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

#Incomplete: Not passing all testcases
#Functions
def mergeIntervals(intervals):
    res = []
    stack = []
    i = 0
    intervals.sort()
    print(intervals)
    n = len(intervals)
    if(n == 1):
        res.append(intervals[n-1])
        return res
    while(i<n):
        print(intervals[i])
        if(len(stack) < 2):
            stack.append(intervals[i])
        elif(len(stack)>=2):
            a = stack.pop()
            b = stack.pop()
            if(a[1]>=b[0]):
                if(a[0]<b[0]):
                    x = a[0]
                else:
                    x = b[0]
                if(a[1]<b[1]):
                    y = b[1]
                else:
                    y = a[1]

                stack.append([x,y])
            else:
                stack.append(b)
                res.append(a)
        i+=1
        # if(a[1]>=b[0]):
        #     if(a[0]<b[0]):
        #         x = a[0]
        #     else:
        #         x = b[0]
        #     if(a[1]<b[1]):
        #         y = b[1]
        #     else:
        #         y = a[1]

        #     res.append([x,y])
        #     i+=1
        # else:
        #     res.append(a)
        #     if(i==n-1):
        #         res.append(b)
        # i+=1
    return res

#Drivers Code
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3]]
# intervals = [[1,4],[0,4]]
# intervals = [[1,4],[0,0]]
intervals = [[1,4],[0,2],[3,5]]
print(intervals)
print(mergeIntervals(intervals))  