# Boolean Parenthesization using Map
import sys
# function
def BPEvaluateTrue(arr,i,j, isTrue):
    result  = 0
    if i>j:
        return False
        
    if i==j:
        if(isTrue == "T"):
            return arr[i] == "T" # Imp step to note
        else:
            return arr[i] == "F" # Imp step to note

    for k in range(i+1 , j ,2): # If we take till j then it will go till j-1
        lt = BPEvaluateTrue(arr,i,k-1, "T")
        rt = BPEvaluateTrue(arr,k+1,j, "T")
        lf = BPEvaluateTrue(arr,i,k-1, "F")
        rf = BPEvaluateTrue(arr,k+1,j, "F")

        if(arr[k] == "&"):
            if(isTrue == "T"):
                result = result + lt*rt 
            else:
                result = result + lt*rf + lf*rt + lf*rf
        
        if(arr[k] == "|"):
            if(isTrue == "T"):
                result = result + lt*rt + lt*rf + lf*rt
            else:
                result = result + lf*rf

        if(arr[k] == "^"):
            if(isTrue == "T"):
                result = result + lt*rf + lf*rt  
            else:
                result = result + lf*rf + lt*rt

    return result
# Drivers code
arr = "T^F&T"
n = len(arr)

print("Total count to evaluate expression to True is,", BPEvaluateTrue(arr,0, n-1, "T"))
#MCM(arr, i, j, isTrue)