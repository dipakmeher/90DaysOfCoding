import sys
def findMaximum(a, m):
    subseq=[]
    for i in range(len(a)):
        temp = []
        temp.append(a[i])
        for j in range(i+1, len(a)):
            temp.append(a[j])
            for z in range(j+1, len(a)):
                temp.append(a[z])
                if(len(temp)==3):
                    subseq.append(tuple(temp))
                    temp.pop()
            temp.pop()
    print(subseq)
    globalMax = 0
    for rec in subseq:
        currMin = sys.maxsize
        for i in range(1,len(rec)):
            currMin = min(abs(a[i]-a[i-1]),currMin)
        print(currMin)
        globalMax = max(globalMax, currMin)
        print(globalMax)
    

#Drivers Code
#Since a is sorted, we can think of applying binary search
# a = [1,2,3,4]
a = [2,3,5,9]
m = 3
print("arr: ",a)
print(findMaximum(a, m))
#Ans 3