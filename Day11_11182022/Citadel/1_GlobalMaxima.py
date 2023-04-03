#https://leetcode.com/discuss/interview-question/1477450/citadel-swe-intern-2022-oa-hackerrank-questions
#https://leetcode.com/discuss/interview-question/1215681/airbnb-oa-global-maximum

import sys
#Functions
def isPossible(a,m,currMax):
    prevMin = a[0]
    m-=1
    for i in range(1, len(a)):
        if m<=0:
            break
        if(a[i] - prevMin >= currMax):
            prevMin = a[i]
            m-=1
    return m==0
def findMaximum(a,m):
    globalMax = 0   
    start = 0
    end = len(a)
    while(start <= end):
        #mid becomes the element to search=> we decide s = m+1 when its possible to 
        #form subsequence till mid of size m. We search of globalMax in later part of the array
        mid = start + (end-start)//2 # currMax
        print("mid: ",mid)
        if(isPossible(a,m, mid)):
            globalMax = mid
            print("GlobalMax: ",globalMax)
            start = mid + 1
            print("start: ",start)
        else:
            end = mid - 1
            print("end: ",end)
    return globalMax

#Drivers Code
#Since a is sorted, we can think of applying binary search
# This answer is calculated based on index
a = [2,3,5,9]
m = 3
print("arr: ",a)
print(findMaximum(a, m))
#Ans 3