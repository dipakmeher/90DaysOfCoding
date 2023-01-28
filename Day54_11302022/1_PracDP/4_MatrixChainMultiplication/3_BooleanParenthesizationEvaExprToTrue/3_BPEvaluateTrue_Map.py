# Boolean Parenthesization using Map
import sys
# function
def BPEvaluateTrue(arr,i,j, isTrue):
    result  = 0
    if i>j:
        return False
    
    if i==j:
        if(isTrue == 1):
            return arr[i] == "T" # Imp step to note
        else:
            return arr[i] == "F" # Imp step to note

    temp = str(i)+" "+str(j)+" "+str(isTrue)
    if(dpDict.keys == temp):
        return dpDict.get(temp)
    

    for k in range(i+1, j,2): # If we take till j then it will go till j-1
        lt = BPEvaluateTrue(arr,i,k-1, 1)
        rt = BPEvaluateTrue(arr,k+1,j, 1)
        lf = BPEvaluateTrue(arr,i,k-1, 0)
        rf = BPEvaluateTrue(arr,k+1,j, 0)

        if(arr[k] == "&"):
            if(isTrue == 1):
                result = result + lt*rt 
            else:
                result = result + lt*rf + lf*rt + lf*rf
        
        if(arr[k] == "|"):
            if(isTrue == 1):
                result = result + lt*rt + lt*rf + lf*rt
            else:
                result = result + lf*rf

        if(arr[k] == "^"):
            if(isTrue == 1):
                result = result + lt*rf + lf*rt  
            else:
                result = result + lf*rf + lt*rt

    dpDict[temp] = result
    return result
# Drivers code
arr = "T^F&T"
n = len(arr)

dpDict = {}
print("Total count to evaluate expression to True is,", BPEvaluateTrue(arr,0, n-1, 1))
#MCM(arr, i, j, isTrue)