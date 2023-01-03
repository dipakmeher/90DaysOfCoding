#Return the Min abs difference between lenghts selected to form a rectangle
import sys 
# Function
def minDifferenceRectange(arr,n):
    countDict = {}
    for i in arr:
        if i in countDict:
            countDict[i] = countDict[i] + 1
        else:
            countDict[i] = 1

    print(countDict)
    singleEle = []
    for key,val in countDict.items():
        if(val>3):
            return 0
        if(val>1):
            singleEle.append(key)
    
    print(singleEle)
    if(len(singleEle) < 2):
        return -1

    singleEle.sort()    
    print(singleEle)
    res = sys.maxsize
    for i in range(1,len(singleEle)):
        res = min(res, int(singleEle[i])-int(singleEle[i-1]))
    
    return res
#Driver Code
arr = [911,1,3,1000,1000,2,2,999,1000,911]
n = len(arr)

print("Min abs difference between lengths involve in forming rectangles are: ", minDifferenceRectange(arr,n))
